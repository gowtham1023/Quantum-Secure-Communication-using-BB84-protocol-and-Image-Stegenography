import React, { useState } from "react";
import Encrypt from "./pages/Encrypt";
import Decrypt from "./pages/Decrypt";
import Navbar from "./components/Navbar";
import "./App.css";

function App() {
  const [page, setPage] = useState("encrypt");

  return (
    <>
      <Navbar setPage={setPage} />

      <div className="container">
        {page === "encrypt" ? <Encrypt /> : <Decrypt />}
      </div>
    </>
  );
}

export default App;