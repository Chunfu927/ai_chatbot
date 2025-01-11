# ai_chatbot
This project is a local language model chatbot application built with React for the frontend and Flask for the backend. The chatbot uses a pre-trained language model to generate responses based on user input.

This README includes sections for getting started, available scripts, project structure, API endpoints, feedback, and license. It provides a comprehensive overview of the project and how to use it.

### presentation：

https://github.com/user-attachments/assets/1692ddb6-ef08-4673-a64f-df6a4674c891


## Table of Contents

- [Getting Started](#getting-started)
- [Available Scripts](#available-scripts)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Feedback](#feedback)
- [License](#license)

## Getting Started

To get started with this project, clone the repository and install the dependencies:

```sh
git clone https://github.com/Chunfu927/ai_chatbot
cd ai_chatbot
npm install
```

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

## Project Structure

```markdown
.gitignore
build/
public/
python_backend/
src/
  App.css
  App.js
  App.test.js
  index.css
  index.js
  reportWebVitals.js
  setupTests.js
package.json
README.md
```

## API Endpoints

### POST /generate

Generate a response from the chatbot.

#### Request Body

```json
{
  "instruction": "Your instruction here",
  "temperature": 0.7,
  "max_length": 100
}
```

#### Response

```json
{
  "instruction": "Your instruction here",
  "generated_text": "Generated text here",
  "fluency": 5,
  "coherence": 5,
  "relevance": 5,
  "diversity": 5
}
```

## Feedback

### POST /feedback

Submit feedback for the chatbot.

#### Request Body

```json
{
  "feedback": "Your feedback here"
}
```

#### Response

```json
{
  "message": "Feedback submitted successfully"
}
```

