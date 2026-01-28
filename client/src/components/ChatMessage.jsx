import ReactMarkdown from 'react-markdown'
import './ChatMessage.css'

function ChatMessage({ message }) {
  const isUser = message.role === 'user'

  return (
    <div className={`message ${isUser ? 'message-user' : 'message-assistant'}`}>
      <div className="message-content">
        {isUser ? (
          <p>{message.content}</p>
        ) : (
          <ReactMarkdown
            components={{
              p: ({ node, ...props }) => <p className="markdown-p" {...props} />,
              h3: ({ node, ...props }) => <h3 className="markdown-h3" {...props} />,
              ul: ({ node, ...props }) => <ul className="markdown-ul" {...props} />,
              li: ({ node, ...props }) => <li className="markdown-li" {...props} />,
              strong: ({ node, ...props }) => <strong className="markdown-strong" {...props} />,
            }}
          >
            {message.content}
          </ReactMarkdown>
        )}
      </div>
    </div>
  )
}

export default ChatMessage
