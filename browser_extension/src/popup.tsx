import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

const Popup: React.FC = () => {
  const [command, setCommand] = useState('');
  const [status, setStatus] = useState('Idle');

  const sendCommand = async () => {
    setStatus('Sending...');
    try {
      chrome.runtime.sendMessage({ type: 'EXECUTE_COMMAND', payload: command }, (response) => {
        if (response && response.success) {
          setStatus('Success');
        } else {
          setStatus('Error: ' + (response?.error || 'Unknown error'));
        }
      });
    } catch (error) {
      setStatus('Failed to send');
    }
  };

  return (
    <div style={{ padding: '20px', width: '300px' }}>
      <h1>FB AI Operator</h1>
      <textarea
        value={command}
        onChange={(e) => setCommand(e.target.value)}
        placeholder="Enter command (e.g., 'Post about AI')"
        rows={4}
        style={{ width: '100%' }}
      />
      <button onClick={sendCommand} style={{ marginTop: '10px', width: '100%' }}>
        Run AI Agent
      </button>
      <p>Status: {status}</p>
    </div>
  );
};

const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<Popup />);
}

export default Popup;
