import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [currentPage, setCurrentPage] = useState('chat'); // 狀態切換
  const [instruction, setInstruction] = useState('');
  const [generatedText, setGeneratedText] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [temperature, setTemperature] = useState(0.7);
  const [maxLength, setMaxLength] = useState(100);

  const [feedback, setFeedback] = useState({
    fluency: 0, /*流暢度fluency*/
    coherence: 0, /*一致性coherence*/
    relevance: 0, /*相關性relevanc*/
    diversity: 0, /*多樣性diversity*/
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!instruction.trim()) return;

    const newInstruction = { text: instruction, type: 'user' };
    setGeneratedText((prev) => [...prev, newInstruction]);
    setInstruction('');
    setIsLoading(true);

    try {
      const response = await axios.post('http://localhost:5000/generate', {
        instruction: newInstruction.text,
        temperature: temperature,
        max_length: maxLength,
      });
      const newGT = { text: response.data.generated_text, type: 'bot' };
      setGeneratedText((prev) => [...prev, newGT]);
    } catch (error) {
      console.error('Error generating text:', error);
    }
    setIsLoading(false);
  };

  const handleFeedbackChange = (metric, value) => {
    setFeedback((prev) => ({ ...prev, [metric]: value }));
  };

  const submitFeedback = async () => {
    try {
      if (!generatedText.length) {
        alert('Generated text is required');
        return;
      }

      // 確保只存取最新的 user 指令
      const userInstruction = generatedText.filter(msg => msg.type === 'user').pop()?.text || '';
      const botResponses = generatedText.filter(msg => msg.type === 'bot').map(msg => msg.text).join('\n');

      await axios.post('http://localhost:5000/feedback', {
        instruction: userInstruction,
        generated_text: botResponses,
        ...feedback,
      });
      alert('Feedback submitted successfully!');
    } catch (error) {
      console.error('Error submitting feedback:', error);
    }
  };

  return (
    <div className="App">
      {currentPage === 'chat' && (
        <div className="chat-container">
          <h1 className="app-title">llama GOGO!</h1>
          <div className="messages">
            {generatedText.map((gentext, index) => (
              <div key={index} className={`message ${gentext.type}`}>
                {gentext.text}
              </div>
            ))}
            {isLoading && <p className="loading-text">我知道你很急，但先別急．．．</p>}
          </div>
          <form onSubmit={handleSubmit} className="chat-input-form">
            <textarea
              className="chat-input"
              value={instruction}
              onChange={(e) => setInstruction(e.target.value)}
              placeholder="你要問啥？"
            />
            <button type="submit" className="send-btn">
              發送
            </button>
          </form>

          <div className="controls">
            <div className="slider-group">
              <label>Temperature: {temperature.toFixed(1)}</label>
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={temperature}
                onChange={(e) => setTemperature(parseFloat(e.target.value))}
                className="slider"
              />
            </div>

            <div className="slider-group">
              <label>最大文本長度: {maxLength}</label>
              <input
                type="range"
                min="10"
                max="500"
                step="10"
                value={maxLength}
                onChange={(e) => setMaxLength(parseInt(e.target.value))}
                className="slider"
              />
            </div>
          </div>
        </div>
      )}

      {currentPage === 'feedback' && (
        <div className="feedback-container">
          <h2>使用感受調查</h2>
          {Object.keys(feedback).map((metric) => (
            <div key={metric} className="feedback-item">
              <label>
                {metric.charAt(0).toUpperCase() + metric.slice(1)}: {feedback[metric]}
              </label>
              <input
                type="range"
                min="0"
                max="5"
                value={feedback[metric]}
                onChange={(e) => handleFeedbackChange(metric, parseInt(e.target.value))}
                className="slider"
              />
            </div>
          ))}
          <button onClick={submitFeedback} className="feedback-btn">
            Submit Feedback
          </button>
        </div>
      )}

      <nav className="bottom-nav">
        <button onClick={() => setCurrentPage('chat')} className={currentPage === 'chat' ? 'active' : ''}>
          對話
        </button>
        <button onClick={() => setCurrentPage('feedback')} className={currentPage === 'feedback' ? 'active' : ''}>
          使用感受調查
        </button>
      </nav>
    </div>
  );
}

export default App;




