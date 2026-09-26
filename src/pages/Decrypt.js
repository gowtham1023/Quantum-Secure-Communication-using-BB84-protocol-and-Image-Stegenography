import React, { useState } from "react";

function Decrypt() {
  const [image, setImage] = useState(null);
  const [key, setKey] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleDecrypt = async () => {
    if (!image || !key) {
      alert("Select image and enter key");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);
    formData.append("bitString", key);

    try {
      setLoading(true);

      const res = await fetch("http://127.0.0.1:5000/decrypt", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (res.ok) {
        setMessage(data.message);
      } else {
        setMessage(""); // clear old message
        alert("❌ Invalid key. Please enter the correct key.");
      }

    } catch (err) {
      console.error(err);
      alert("❌ Enter the correct stego image");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h2>🔓 Secure Decryption</h2>

        {/* 📤 Image Upload */}
        <input
          type="file"
          onChange={(e) => setImage(e.target.files[0])}
        />

        {image && (
          <p style={{ marginTop: "10px", fontSize: "13px" }}>
            📁 Selected: {image.name}
          </p>
        )}

        {/* 🔑 Key Input */}
        <input
          type="text"
          placeholder="Enter Bit String (Key)..."
          value={key}
          onChange={(e) => setKey(e.target.value)}
        />

        {/* 🚀 Button */}
        <button className="main-btn" onClick={handleDecrypt}>
  Decrypt Message
</button>

        {/* 📩 Output */}
        {message && (
          <>
            <p>📩 Decrypted Message:</p>
            <div className="output">{message}</div>
          </>
        )}
      </div>
    </div>
  );
}

export default Decrypt;