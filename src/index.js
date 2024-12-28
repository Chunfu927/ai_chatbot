import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById('root')); // 確保根元素 ID 是 'root'
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
/*ReactDOM.render(
  <React.StrictMode>
    {" "}
    <App />{" "}
  </React.StrictMode>,
  document.getElementById("root")
);*/
