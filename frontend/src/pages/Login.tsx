import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api/auth";

interface LoginFormData {
  username: string;
  password: string;
}

interface LoginResponse {
  token?: string;
  access_token?: string;
  user?: {
    id?: string | number;
    username?: string;
    name?: string;
  };
  message?: string;
}

export default function Login() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState<LoginFormData>({
    username: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    const { name, value } = e.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));

    if (error) {
      setError("");
    }
  };

  const handleSubmit = async (
    e: FormEvent<HTMLFormElement>
  ) => {
    e.preventDefault();

    setError("");

    // Validate username
    if (!formData.username.trim()) {
      setError("Please enter your username.");
      return;
    }

    // Validate password
    if (!formData.password) {
      setError("Please enter your password.");
      return;
    }

    try {
      setLoading(true);

      const response: LoginResponse =
        await login(formData);

      // Get token from backend response
      const token =
        response.token || response.access_token;

      if (!token) {
        setError(
          "Login failed. Authentication token was not received."
        );
        return;
      }

      // Save authentication token
      localStorage.setItem("token", token);

      // Save user information
      if (response.user) {
        localStorage.setItem(
          "user",
          JSON.stringify(response.user)
        );
      }

      // Redirect to Dashboard
      navigate("/dashboard", {
        replace: true,
      });
    } catch (err: any) {
      console.error("Login failed:", err);

      const message =
        err?.response?.data?.message ||
        err?.response?.data?.detail ||
        err?.response?.data?.error ||
        "Invalid username or password.";

      setError(message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.page}>
      <div style={styles.card}>

        {/* Logo */}
        <div style={styles.logoContainer}>
          <div style={styles.logo}>
            📈
          </div>

          <h1 style={styles.title}>
            StockScanner Pro
          </h1>

          <p style={styles.subtitle}>
            Sign in to your account
          </p>
        </div>

        {/* Login Form */}
        <form onSubmit={handleSubmit}>

          {/* Error */}
          {error && (
            <div style={styles.error}>
              {error}
            </div>
          )}

          {/* Username */}
          <div style={styles.formGroup}>
            <label
              htmlFor="username"
              style={styles.label}
            >
              Username
            </label>

            <input
              id="username"
              name="username"
              type="text"
              placeholder="Enter your username"
              value={formData.username}
              onChange={handleChange}
              autoComplete="username"
              disabled={loading}
              style={styles.input}
            />
          </div>

          {/* Password */}
          <div style={styles.formGroup}>
            <label
              htmlFor="password"
              style={styles.label}
            >
              Password
            </label>

            <input
              id="password"
              name="password"
              type="password"
              placeholder="Enter your password"
              value={formData.password}
              onChange={handleChange}
              autoComplete="current-password"
              disabled={loading}
              style={styles.input}
            />
          </div>

          {/* Forgot Password */}
          <div style={styles.forgotContainer}>
            <button
              type="button"
              style={styles.forgotButton}
              onClick={() => {
                alert(
                  "Forgot password functionality is not implemented yet."
                );
              }}
            >
              Forgot Password?
            </button>
          </div>

          {/* Login Button */}
          <button
            type="submit"
            disabled={loading}
            style={{
              ...styles.loginButton,
              ...(loading
                ? styles.loginButtonDisabled
                : {}),
            }}
          >
            {loading
              ? "Signing in..."
              : "Sign In"}
          </button>

        </form>

        {/* Footer */}
        <div style={styles.footer}>
          © {new Date().getFullYear()} StockScanner Pro
        </div>

      </div>
    </div>
  );
}


/* =========================
   Styles
========================= */

const styles: {
  [key: string]: React.CSSProperties;
} = {

  page: {
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f4f7fb",
    padding: "20px",
    boxSizing: "border-box",
  },

  card: {
    width: "100%",
    maxWidth: "420px",
    backgroundColor: "#ffffff",
    padding: "40px",
    borderRadius: "12px",
    boxShadow:
      "0 10px 30px rgba(0, 0, 0, 0.1)",
    boxSizing: "border-box",
  },

  logoContainer: {
    textAlign: "center",
    marginBottom: "30px",
  },

  logo: {
    fontSize: "48px",
    marginBottom: "10px",
  },

  title: {
    margin: "0",
    fontSize: "28px",
    fontWeight: 700,
    color: "#1f2937",
  },

  subtitle: {
    marginTop: "8px",
    color: "#6b7280",
    fontSize: "15px",
  },

  formGroup: {
    marginBottom: "20px",
  },

  label: {
    display: "block",
    marginBottom: "8px",
    fontSize: "14px",
    fontWeight: 600,
    color: "#374151",
  },

  input: {
    width: "100%",
    padding: "12px 14px",
    border: "1px solid #d1d5db",
    borderRadius: "8px",
    fontSize: "15px",
    outline: "none",
    boxSizing: "border-box",
  },

  forgotContainer: {
    textAlign: "right",
    marginBottom: "20px",
  },

  forgotButton: {
    border: "none",
    background: "transparent",
    color: "#2563eb",
    cursor: "pointer",
    fontSize: "14px",
    padding: 0,
  },

  loginButton: {
    width: "100%",
    padding: "13px",
    border: "none",
    borderRadius: "8px",
    backgroundColor: "#2563eb",
    color: "#ffffff",
    fontSize: "16px",
    fontWeight: 600,
    cursor: "pointer",
  },

  loginButtonDisabled: {
    opacity: 0.6,
    cursor: "not-allowed",
  },

  error: {
    backgroundColor: "#fee2e2",
    color: "#b91c1c",
    padding: "12px",
    borderRadius: "8px",
    marginBottom: "20px",
    fontSize: "14px",
  },

  footer: {
    textAlign: "center",
    marginTop: "30px",
    color: "#9ca3af",
    fontSize: "13px",
  },
};
