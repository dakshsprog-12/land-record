import { useNavigate } from "react-router-dom";
import card1Img from "../assets/heroimg1.png";
import card2Img from "../assets/heroimg2.png";
import card3Img from "../assets/heroimg3.png";


export default function HomePage() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        minHeight: "100vh",
        width: "100%",
        backgroundColor: "#ffffff",
        color: "#111827",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        fontFamily:
          '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
        margin: 0,
        padding: 0,
        boxSizing: "border-box",
      }}
    >
      {/* 1. Header Navigation Bar */}
      <header
        style={{
          width: "100%",
          maxWidth: "1100px",
          padding: "1.6rem 2rem 0 2rem",
          boxSizing: "border-box",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            paddingBottom: "0.85rem",
            borderBottom: "1px solid #d4d4d8",
          }}
        >
          <h1
            style={{
              fontSize: "30px",
              fontWeight: "900",
              letterSpacing: "1.2px",
              color: "#000000",
              textTransform: "uppercase",
              margin: 0,
            }}
          >
            Bhumi Setu
          </h1>

          <nav
            style={{
              display: "flex",
              alignItems: "center",
              gap: "2.75rem",
            }}
          >
            <a
              href="/HomePage"
              style={{
                fontSize: "15px",
                fontWeight: "700",
                letterSpacing: "1px",
                color: "#18181b",
                textDecoration: "none",
                transition: "color 0.2s ease",
              }}
              onMouseOver={(e) => (e.currentTarget.style.color = "#000000")}
              onMouseOut={(e) => (e.currentTarget.style.color = "#18181b")}
            >
              HOME
            </a>
            <a
              href="#contact"
              style={{
                fontSize: "15px",
                fontWeight: "700",
                letterSpacing: "1px",
                color: "#18181b",
                textDecoration: "none",
                transition: "color 0.2s ease",
              }}
              onMouseOver={(e) => (e.currentTarget.style.color = "#000000")}
              onMouseOut={(e) => (e.currentTarget.style.color = "#18181b")}
            >
              CONTACT US
            </a>
            <a
              href="#about"
              style={{
                fontSize: "15px",
                fontWeight: "700",
                letterSpacing: "1px",
                color: "#18181b",
                textDecoration: "none",
                transition: "color 0.2s ease",
              }}
              onMouseOver={(e) => (e.currentTarget.style.color = "#000000")}
              onMouseOut={(e) => (e.currentTarget.style.color = "#18181b")}
            >
              ABOUT US
            </a>
          </nav>
        </div>
      </header>

      {/* 2. Hero Section */}
      <main
        style={{
          width: "100%",
          maxWidth: "1100px",
          padding: "4rem 2rem",
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "space-between",
          gap: "2.5rem",
          boxSizing: "border-box",
          flex: 1,
        }}
      >
        {/* Left Column: Heading, Subtitle & Action Button */}
        <div
          style={{
            flex: "0 0 45%",
            display: "flex",
            flexDirection: "column",
            alignItems: "flex-start",
            zIndex: 10,
          }}
        >
          <h2
            style={{
              fontSize: "52px",
              fontWeight: "900",
              letterSpacing: "-1.5px",
              lineHeight: "1.08",
              color: "#09090b",
              margin: "0 0 1.25rem 0",
            }}
          >
            Land Record <br />
            Digitizer
          </h2>

          <p
            style={{
              fontSize: "15px",
              lineHeight: "1.6",
              color: "#52525b",
              maxWidth: "380px",
              margin: "0 0 2.25rem 0",
            }}
          >
            Simplifying land record administration through automated document
            processing, secure data extraction, and hassle-free status tracking.
          </p>

          <button
            type="button"
            onClick={() => navigate("/register")}
            style={{
              padding: "11px 28px",
              borderRadius: "9999px",
              border: "1px solid #d4d4d8",
              backgroundColor: "#e4e4e7",
              fontSize: "12px",
              fontWeight: "800",
              letterSpacing: "1px",
              textTransform: "uppercase",
              color: "#18181b",
              cursor: "pointer",
              boxShadow: "0 2px 4px rgba(0, 0, 0, 0.06)",
              transition: "all 0.2s ease",
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.backgroundColor = "#d4d4d8";
              e.currentTarget.style.transform = "scale(1.02)";
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.backgroundColor = "#e4e4e7";
              e.currentTarget.style.transform = "scale(1)";
            }}
          >
            Create Account
          </button>
        </div>

        {/* Right Column: 3 Layered Staggered Cards */}
        <div
          style={{
            flex: "0 0 55%",
            position: "relative",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            minHeight: "440px",
          }}
        >
          {/* Ambient Blurred Spheres */}
          <div
            style={{
              position: "absolute",
              left: "-15px",
              top: "20%",
              width: "120px",
              height: "120px",
              borderRadius: "50%",
              background: "rgba(203, 213, 225, 0.6)",
              filter: "blur(35px)",
              pointerEvents: "none",
              zIndex: 0,
            }}
          />
          <div
            style={{
              position: "absolute",
              right: "0px",
              bottom: "10%",
              width: "140px",
              height: "140px",
              borderRadius: "50%",
              background: "rgba(219, 234, 254, 0.5)",
              filter: "blur(40px)",
              pointerEvents: "none",
              zIndex: 0,
            }}
          />

          {/* Card 1 (Left - Back) */}
          <div
            style={{
              width: "185px",
              height: "360px",
              backgroundColor: "#f4f4f5",
              borderRadius: "4px",
              overflow: "hidden",
              border: "1px solid #e4e4e7",
              boxShadow: "0 8px 16px -4px rgba(0, 0, 0, 0.1)",
              position: "relative",
              zIndex: 1,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <img
              src={card1Img}
              alt="Cadastral Map"
              style={{ width: "100%", height: "100%", objectFit: "cover", display: "block", }}
              onError={(e) => {
                e.currentTarget.style.display = "none";
                e.currentTarget.parentElement.innerText = "Card 1";
              }}
            />
          </div>

          {/* Card 2 (Center - Front & Elevated) */}
          <div
            style={{
              width: "205px",
              height: "410px",
              backgroundColor: "#fafafa",
              borderRadius: "4px",
              overflow: "hidden",
              border: "1px solid #e4e4e7",
              boxShadow: "0 22px 35px -8px rgba(0, 0, 0, 0.18)",
              position: "relative",
              zIndex: 2,
              marginLeft: "-40px",
              marginTop: "-30px",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <img
              src={card2Img}
              alt="Land Registry"
              style={{ width: "100%", height: "100%", objectFit: "cover", display: "block" }}
              onError={(e) => {
                e.currentTarget.style.display = "none";
                e.currentTarget.parentElement.innerText = "Card 2";
              }}
            />
          </div>

          {/* Card 3 (Right - Lower Offset) */}
          <div
            style={{
              width: "185px",
              height: "360px",
              backgroundColor: "#f4f4f5",
              borderRadius: "4px",
              overflow: "hidden",
              border: "1px solid #e4e4e7",
              boxShadow: "0 8px 16px -4px rgba(0, 0, 0, 0.1)",
              position: "relative",
              zIndex: 1,
              marginLeft: "-40px",
              marginTop: "48px",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <img
              src={card3Img}
              alt="Digital Records"
              style={{ width: "100%", height: "100%", objectFit: "cover", display: "block" }}
              onError={(e) => {
                e.currentTarget.style.display = "none";
                e.currentTarget.parentElement.innerText = "Card 3";
              }}
            />
          </div>
        </div>
      </main>
    </div>
  );
}