// background.ts

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'EXECUTE_COMMAND') {
    executeOnLocalAgent(message.payload)
      .then(result => sendResponse({ success: true, result }))
      .catch(error => sendResponse({ success: false, error: error.message }));
    return true; // Keep message channel open
  }
});

async function executeOnLocalAgent(command: string) {
  const LOCAL_AGENT_URL = 'http://localhost:8000/execute';

  // First, get the plan from Cloud Brain via Local Agent (or directly if simplified)
  // In this architecture, Local Agent forwards to Cloud Brain

  const response = await fetch(LOCAL_AGENT_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task: command, steps: [] }) // Simplified
  });

  if (!response.ok) {
    throw new Error('Failed to connect to local executor');
  }

  return await response.json();
}
