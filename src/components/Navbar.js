import React from "react";

function Navbar({ setPage }) {
  return (
    <div className="navbar">
      <h2>🔐Quantum Stego</h2>
      <p>Protect your data using Quantum Key Distribution & Steganography</p>
      <div>
        <a onClick={() => setPage("encrypt")}>Encrypt</a>
        <a onClick={() => setPage("decrypt")}>Decrypt</a>
      </div>
    </div>
  );
}

export default Navbar;