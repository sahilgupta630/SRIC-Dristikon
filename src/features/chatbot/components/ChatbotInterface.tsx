import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { MessageCircle, Send, X, Bot, User, Sparkles, FileText, Search, Loader2, Paperclip, ChevronRight } from 'lucide-react';

interface Message {
  id: string;
  type: 'user' | 'bot';
  content: string;
  timestamp: Date;
  loading?: boolean;
  context?: string;
  sources?: Array<{ title: string; page: number }>;
}

interface ChatbotInterfaceProps {
  isOpen: boolean;
  onToggle: () => void;
}

const sampleQueries = [
  "How can I purchase equipment worth ₹5 lakhs?",
  "SRIC project frameworks?",
  "Vendor registration process?",
  "Documents needed for the purchase of spare parts?"
];

// Bot responses removed - using API


export function ChatbotInterface({ isOpen, onToggle }: ChatbotInterfaceProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      type: 'bot',
      content: "👋 Hello! I'm the SRIC Compass. I can help you with:\n\n• Purchase procedures and guidelines\n• Project information and funding\n• Patent filing requirements\n• Vendor registration\n• General SRIC queries\n\nHow can I assist you today?",
      timestamp: new Date()
    }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (isOpen && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isOpen]);



  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: input,
      timestamp: new Date()
    };

    setMessages((prev: Message[]) => [...prev, userMessage]);
    setInput('');
    setIsTyping(true);

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: userMessage.content,
          history: messages.map((m: Message) => ({
            role: m.type,
            content: m.content
          }))
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();

      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'bot',
        content: data.answer,
        timestamp: new Date(),
        context: "Purchase Document",
        sources: data.sources?.map((s: any) => ({
          title: s.metadata?.source || "Document",
          page: s.metadata?.page || 1
        }))
      };

      setMessages((prev: Message[]) => [...prev, botMessage]);
    } catch (error) {
      console.error('Error fetching chat response:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'bot',
        content: "I apologize, but I'm having trouble connecting to the server. Please ensure the backend is running.",
        timestamp: new Date()
      };
      setMessages((prev: Message[]) => [...prev, errorMessage]);
    } finally {
      setIsTyping(false);
    }
  };

  const handleQuickQuery = (query: string) => {
    setInput(query);
    setTimeout(() => handleSend(), 100);
  };

  return (
    <>
      {/* Side Panel */}
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ x: '100%' }}
            animate={{ x: 0 }}
            exit={{ x: '100%' }}
            transition={{ type: 'spring', damping: 25, stiffness: 200 }}
            className="fixed top-0 right-0 h-full w-[400px] bg-gradient-to-br from-slate-800 to-slate-900 shadow-2xl border-l border-white/20 z-50 flex flex-col"
          >
            {/* Header */}
            <div className="bg-gradient-to-r from-blue-600 to-purple-600 p-4 flex items-center justify-between flex-shrink-0">
              <div className="flex items-center gap-3">
                <motion.div
                  animate={{ rotate: [0, 10, -10, 0] }}
                  transition={{ repeat: Infinity, duration: 3 }}
                  className="w-10 h-10 bg-white rounded-full flex items-center justify-center"
                >
                  <Bot className="w-6 h-6 text-blue-600" />
                </motion.div>
                <div>
                  <h3 className="text-white">SRIC Compass</h3>
                  <div className="flex items-center gap-2">
                    <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
                    <span className="text-blue-100 text-xs">Online</span>
                  </div>
                </div>
              </div>
              <button
                onClick={onToggle}
                className="p-2 hover:bg-white/20 rounded-lg transition-colors"
              >
                <X className="w-5 h-5 text-white" />
              </button>
            </div>

            {/* Messages */}
            <div className="flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar">
              {messages.map((message: Message, index: number) => (
                <motion.div
                  key={message.id}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.05 }}
                  className={`flex gap-2 ${message.type === 'user' ? 'flex-row-reverse' : 'flex-row'}`}
                >
                  {/* Avatar */}
                  <div className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
                    message.type === 'bot' 
                      ? 'bg-gradient-to-br from-blue-500 to-purple-600' 
                      : 'bg-gradient-to-br from-green-500 to-emerald-600'
                  }`}>
                    {message.type === 'bot' ? (
                      <Bot className="w-4 h-4 text-white" />
                    ) : (
                      <User className="w-4 h-4 text-white" />
                    )}
                  </div>

                  {/* Message Content */}
                  <div className={`flex flex-col ${message.type === 'user' ? 'items-end' : 'items-start'} max-w-[75%]`}>
                    <div className={`rounded-xl p-3 ${
                      message.type === 'bot'
                        ? 'bg-slate-700/50 border border-white/10'
                        : 'bg-gradient-to-br from-blue-600 to-purple-600'
                    }`}>
                      <p className="text-white text-xs whitespace-pre-wrap leading-relaxed">{message.content}</p>
                    </div>
                    
                    {/* Context & Sources */}
                    {message.type === 'bot' && message.context && (
                      <div className="mt-1 flex items-center gap-1 text-xs text-slate-400">
                        <Sparkles className="w-3 h-3" />
                        <span className="text-xs">{message.context}</span>
                      </div>
                    )}
                    
                    {message.sources && message.sources.length > 0 && (
                      <div className="mt-1 space-y-1">
                        {message.sources.map((source: any, idx: number) => (
                          <div key={idx} className="flex items-center gap-1 text-xs text-slate-400 bg-slate-700/30 px-2 py-1 rounded">
                            <FileText className="w-3 h-3" />
                            <span className="text-xs">{source.title} (p.{source.page})</span>
                          </div>
                        ))}
                      </div>
                    )}

                    <span className="text-xs text-slate-500 mt-1">
                      {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                    </span>
                  </div>
                </motion.div>
              ))}

              {/* Typing Indicator */}
              {isTyping && (
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="flex gap-2"
                >
                  <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
                    <Bot className="w-4 h-4 text-white" />
                  </div>
                  <div className="bg-slate-700/50 border border-white/10 rounded-xl p-3">
                    <div className="flex gap-1">
                      <motion.div
                        animate={{ scale: [1, 1.5, 1] }}
                        transition={{ repeat: Infinity, duration: 1, delay: 0 }}
                        className="w-2 h-2 bg-blue-400 rounded-full"
                      />
                      <motion.div
                        animate={{ scale: [1, 1.5, 1] }}
                        transition={{ repeat: Infinity, duration: 1, delay: 0.2 }}
                        className="w-2 h-2 bg-blue-400 rounded-full"
                      />
                      <motion.div
                        animate={{ scale: [1, 1.5, 1] }}
                        transition={{ repeat: Infinity, duration: 1, delay: 0.4 }}
                        className="w-2 h-2 bg-blue-400 rounded-full"
                      />
                    </div>
                  </div>
                </motion.div>
              )}

              <div ref={messagesEndRef} />
            </div>

            {/* Quick Queries */}
            <div className="px-4 py-2 border-t border-white/10 flex-shrink-0">
              <div className="flex items-center gap-2 mb-2">
                <Search className="w-3 h-3 text-slate-400" />
                <span className="text-slate-400 text-xs">Quick queries:</span>
              </div>
              <div className="flex flex-wrap gap-1">
                {sampleQueries.map((query, idx) => (
                  <motion.button
                    key={idx}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    onClick={() => handleQuickQuery(query)}
                    className="px-2 py-1 bg-slate-700/50 hover:bg-slate-700 text-slate-300 text-xs rounded transition-colors"
                  >
                    {query}
                  </motion.button>
                ))}
              </div>
            </div>

            {/* Input Area */}
            <div className="p-4 border-t border-white/10 bg-slate-800/50 flex-shrink-0">
              <div className="flex gap-2 mb-2">
                <button className="p-2 hover:bg-slate-700/50 rounded-lg transition-colors">
                  <Paperclip className="w-4 h-4 text-slate-400" />
                </button>
                <input
                  ref={inputRef}
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                  placeholder="Ask about SRIC procedures..."
                  className="flex-1 bg-slate-700/50 border border-white/10 rounded-lg px-3 py-2 text-white text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={handleSend}
                  disabled={!input.trim() || isTyping}
                  className={`p-2 rounded-lg transition-all ${
                    input.trim() && !isTyping
                      ? 'bg-gradient-to-r from-blue-600 to-purple-600 hover:shadow-lg'
                      : 'bg-slate-700/50 cursor-not-allowed'
                  }`}
                >
                  {isTyping ? (
                    <Loader2 className="w-4 h-4 text-slate-400 animate-spin" />
                  ) : (
                    <Send className="w-4 h-4 text-white" />
                  )}
                </motion.button>
              </div>
              <p className="text-xs text-slate-500 text-center">
                AI-powered • SRIC documents
              </p>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <style>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(51, 65, 85, 0.3);
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(99, 102, 241, 0.5);
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(99, 102, 241, 0.7);
        }
      `}</style>
    </>
  );
}