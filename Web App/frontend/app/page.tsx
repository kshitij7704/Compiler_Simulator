'use client'; // Marks this component as a Client Component

import { useState } from 'react';
import './globals.css';

export default function Home() {
  const [sourceCode, setSourceCode] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:5000/compile', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({ source_code: sourceCode }),
      });
      if (!response.ok) {
        throw new Error('Failed to compile');
      }
      const result = await response.json();
      setOutput(result.output);
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'An unknown error occurred';
      setOutput(`Error: ${errorMessage}`);
    }
    setLoading(false);
  };

  const formatOutput = (outputText: string) => {
    if (!outputText) return null;

    const sections = outputText.split('\n\n').filter(Boolean);
    return sections.map((section, index) => {
      const lines = section.split('\n');
      const header = lines[0].match(/^\[(.+)\]$/) || lines[0].startsWith('Source Code') || lines[0].startsWith('Error:');
      const title = header ? (header[1] || lines[0]) : null;
      const content = title ? lines.slice(1) : lines;

      return (
        <div
          key={index}
          className="mb-6 transform transition-all duration-300 hover:scale-105 hover:shadow-xl"
        >
          {title && (
            <h3 className="text-lg font-semibold text-gray-100 bg-gradient-to-r from-gray-800 to-gray-700 px-4 py-2 rounded-t-md border-b border-gray-600">
              {title}
            </h3>
          )}
          <pre className="bg-gray-900 text-gray-200 p-4 rounded-b-md overflow-x-auto whitespace-pre-wrap border border-gray-700">
            {content.map((line, i) => (
              <div
                key={i}
                className="text-sm transition-colors duration-200 hover:text-blue-300"
              >
                {line}
              </div>
            ))}
          </pre>
        </div>
      );
    });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-100 to-gray-200 flex flex-col items-center py-12 px-4">
      <div className="w-full max-w-4xl bg-white rounded-xl shadow-2xl p-8 transform transition-all duration-500 hover:shadow-3xl">
        <h1 className="text-4xl font-extrabold text-gray-900 mb-8 text-center tracking-tight animate-fade-in-down">
          Compiler Simulator
        </h1>

        <form onSubmit={handleSubmit} className="space-y-8">
          <div>
            <label
              htmlFor="sourceCode"
              className="block text-sm font-medium text-gray-700 mb-2 transition-all duration-300 hover:text-blue-600"
            >
              Enter Source Code
            </label>
            <textarea
              id="sourceCode"
              value={sourceCode}
              onChange={(e) => setSourceCode(e.target.value)}
              className="w-full h-48 p-4 border border-gray-300 rounded-lg focus:ring-4 focus:ring-blue-500 focus:border-blue-500 resize-y shadow-sm transition-all duration-300 hover:shadow-md focus:shadow-lg"
              placeholder="e.g., x = 5 + 3;"
            />
          </div>

          <button
            type="submit"
            disabled={loading || !sourceCode.trim()}
            className={`w-full py-4 px-6 rounded-lg text-white font-semibold transition-all duration-300 transform ${
              loading || !sourceCode.trim()
                ? 'bg-gray-400 cursor-not-allowed'
                : 'bg-blue-600 hover:bg-blue-700 hover:scale-105 active:scale-95 shadow-lg hover:shadow-xl'
            }`}
          >
            {loading ? (
              <span className="flex items-center justify-center">
                <svg
                  className="animate-spin h-5 w-5 mr-2 text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  />
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8v8h8a8 8 0 01-8 8 8 8 0 01-8-8z"
                  />
                </svg>
                Compiling...
              </span>
            ) : (
              'Compile'
            )}
          </button>
        </form>

        {output && (
          <div className="mt-10 animate-fade-in-up">
            <h2 className="text-2xl font-bold text-gray-800 mb-6 border-b-2 border-blue-500 pb-2">
              Compiler Output
            </h2>
            <div className="bg-gray-900 text-white p-6 rounded-lg shadow-inner">
              {formatOutput(output)}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}