"use client";

import { useEffect, useState } from "react";

export default function Home() {

  const [emails, setEmails] = useState<any[]>([]);
  const [selectedThread, setSelectedThread] = useState<any>(null);
  const [threadEmails, setThreadEmails] = useState<any[]>([]);
  const [aiReply, setAiReply] = useState("");

  useEffect(() => {

    fetch("http://127.0.0.1:8000/api/emails")
      .then((response) => response.json())
      .then((data) => {
        setEmails(data);
      });

  }, []);

  const fetchThread = (threadId: string) => {

    fetch(`http://127.0.0.1:8000/api/thread/${threadId}`)
      .then((response) => response.json())
      .then((data) => {

        setSelectedThread(threadId);
        setThreadEmails(data.emails);

      });
  };

  const generateReply = () => {

    fetch(`http://127.0.0.1:8000/api/reply/${selectedThread}`)
      .then((response) => response.json())
      .then((data) => {
        setAiReply(data.reply);
      });

  };

  return (

    <main className="min-h-screen bg-gray-100 p-10 text-black">

      <h1 className="text-5xl font-bold text-black mb-3">
        SenAI CRM Intelligence Platform
      </h1>

      <p className="text-gray-700 mb-10 text-lg">
        AI-powered CRM intelligence dashboard for support operations.
      </p>

      <h2 className="text-2xl font-bold mb-6">
        Emails
      </h2>

      <div className="space-y-4">

        {emails.map((email, index) => (

          <div
            key={index}
            onClick={() => fetchThread(email.thread_id)}
            className="bg-white p-6 rounded-xl shadow-lg cursor-pointer hover:bg-gray-200 transition"
          >

            <h3 className="text-xl font-bold">
              {email.subject}
            </h3>

            <p className="mt-2">
              {email.summary}
            </p>

            <div className="flex gap-4 mt-4">

              <span className="bg-red-100 text-red-600 px-3 py-1 rounded-full">
                Priority: {email.priority}
              </span>

              <span className="bg-yellow-100 text-yellow-700 px-3 py-1 rounded-full">
                Sentiment: {email.sentiment}
              </span>

            </div>

          </div>

        ))}

      </div>

      {selectedThread && (

        <div className="bg-white p-6 rounded-xl shadow-lg mt-10">

          <h2 className="text-3xl font-bold mb-4">
            Conversation Thread
          </h2>

          <button
            onClick={generateReply}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 mb-6"
          >
            Generate AI Reply
          </button>

          <div className="space-y-4">

            {threadEmails.map((email, index) => (

              <div
                key={index}
                className="border p-4 rounded-lg"
              >

                <h3 className="font-bold text-lg">
                  {email.subject}
                </h3>

                <p className="mt-2">
                  {email.body}
                </p>

              </div>

            ))}

          </div>

          {aiReply && (

            <div className="bg-blue-100 p-4 rounded-lg mt-6">

              <h3 className="font-bold text-xl mb-2">
                AI Suggested Reply
              </h3>

              <p>
                {aiReply}
              </p>

            </div>

          )}

        </div>

      )}

    </main>

  );
}