import { useState } from "react";
import axios from "axios";

function Encrypt() {
  const [message, setMessage] = useState("");
  const [image, setImage] = useState(null);

  const [key, setKey] = useState("");
  const [bitString, setBitString] = useState("");
  const [stegoUrl, setStegoUrl] = useState("");

  const [loading, setLoading] = useState(false);

  const handleEncrypt = async () => {
    if (!message || !image) {
      alert("Enter message and select image");
      return;
    }

    const formData = new FormData();
    formData.append("message", message);
    formData.append("image", image);

    try {
      setLoading(true);

      const res = await axios.post(
        "http://127.0.0.1:5000/encrypt",
        formData
      );

      setKey(res.data.key);
      setBitString(res.data.bitString);

      // important: cache busting
      setStegoUrl("http://127.0.0.1:5000/stego?" + new Date().getTime());

    } catch (err) {
      console.error(err);
      alert("Encryption failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h2>🔐 Secure Encryption</h2>
        <textarea
          placeholder="Enter secret message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

        <input
          type="file"
          onChange={(e) => setImage(e.target.files[0])}
        />

        <button className="main-btn" onClick={handleEncrypt}>
  Encrypt & Download
</button>

        {key && (
          <div className="output">
            <b>🔑 Key:</b> {key}
          </div>
        )}

        {bitString && (
          <div className="output">
            <b>📊 Bit String:</b> {bitString}
          </div>
        )}

        {stegoUrl && (
          <>
            <p>🖼 Stego Image:</p>
            <img src={stegoUrl} alt="Stego Output" />
          </>
        )}
      </div>
    </div>
  );
}

export default Encrypt;