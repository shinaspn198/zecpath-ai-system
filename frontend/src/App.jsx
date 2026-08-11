import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [parsing, setParsing] = useState(false);

  const [candidate, setCandidate] = useState(null);
  const [profile, setProfile] = useState(null);

  const [error, setError] = useState("");

  // ==============================
  // Upload Resume
  // ==============================

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a resume first.");
      return;
    }

    setUploading(true);
    setError("");
    setCandidate(null);
    setProfile(null);

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/resume/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Resume upload failed.");
      }

      setCandidate(data);

    } catch (err) {
      setError(err.message);

    } finally {
      setUploading(false);
    }
  };


  // ==============================
  // Parse Resume
  // ==============================

  const handleParse = async () => {
    if (!candidate?.candidate_id) {
      setError("Candidate ID is missing.");
      return;
    }

    setParsing(true);
    setError("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/resume/parse",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            candidate_id: candidate.candidate_id,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Resume parsing failed.");
      }

      setProfile(data.profile);

    } catch (err) {
      setError(err.message);

    } finally {
      setParsing(false);
    }
  };


  // ==============================
  // Render
  // ==============================

  return (
    <div className="app">

      {/* Header */}

      <header className="header">

        <div>
          <h1>Zecpath AI</h1>
          <p>AI Recruitment Platform</p>
        </div>

      </header>


      <main className="main">

        {/* Hero */}

        <section className="hero">

          <span className="badge">
            AI-POWERED RECRUITMENT
          </span>

          <h2>
            Resume Intelligence
          </h2>

          <p>
            Upload a candidate resume and let Zecpath AI
            transform it into structured recruitment data.
          </p>

        </section>


        {/* Upload */}

        <section className="upload-card">

          <div className="upload-icon">
            📄
          </div>

          <h3>
            Upload Candidate Resume
          </h3>

          <p>
            Supported formats: PDF and DOCX
          </p>


          <input
            type="file"
            accept=".pdf,.docx"
            onChange={(event) => {

              setFile(event.target.files[0]);

              setError("");
              setCandidate(null);
              setProfile(null);

            }}
          />


          {file && (

            <div className="selected-file">

              Selected:{" "}

              <strong>
                {file.name}
              </strong>

            </div>

          )}


          {/* Upload Button */}

          <button
            onClick={handleUpload}
            disabled={uploading}
          >

            {uploading
              ? "Uploading..."
              : "Upload Resume"}

          </button>


          {/* Upload Success */}

          {candidate && (

            <div className="success">

              <h3>
                Resume Uploaded Successfully
              </h3>

              <p>
                <strong>Candidate ID:</strong>{" "}
                {candidate.candidate_id}
              </p>

              <p>
                <strong>Filename:</strong>{" "}
                {candidate.filename}
              </p>

              <p>
                <strong>Status:</strong>{" "}
                {candidate.status}
              </p>


              {/* Parse Button */}

              <button
                onClick={handleParse}
                disabled={parsing}
              >

                {parsing
                  ? "Parsing Resume..."
                  : "Parse Resume"}

              </button>

            </div>

          )}


          {/* Error */}

          {error && (

            <div className="error">

              {error}

            </div>

          )}

        </section>


        {/* Candidate Profile */}

        {profile && (

          <section className="profile-card">

            <div className="profile-header">

              <span className="badge">
                RESUME PARSED
              </span>

              <h2>
                Candidate Profile
              </h2>

              <p>
                Structured candidate information extracted
                from the uploaded resume.
              </p>

            </div>


            {/* Basic Information */}

            <div className="profile-section">

              <h3>
                👤 Basic Information
              </h3>

              <div className="profile-grid">

                <div>
                  <span>Name</span>
                  <strong>
                    {profile.name || "Not detected"}
                  </strong>
                </div>

                <div>
                  <span>Email</span>
                  <strong>
                    {profile.email || "Not detected"}
                  </strong>
                </div>

                <div>
                  <span>Phone</span>
                  <strong>
                    {profile.phone || "Not detected"}
                  </strong>
                </div>

                <div>
                  <span>Location</span>
                  <strong>
                    {profile.location || "Not detected"}
                  </strong>
                </div>

              </div>

            </div>


            {/* Summary */}

            {profile.summary && (

              <div className="profile-section">

                <h3>
                  📝 Summary
                </h3>

                <p className="profile-text">
                  {profile.summary}
                </p>

              </div>

            )}


            {/* Skills */}

            <div className="profile-section">

              <h3>
                🛠 Skills
              </h3>

              <div className="tag-container">

                {profile.skills?.length > 0 ? (

                  profile.skills.map((skill, index) => (

                    <span
                      className="tag"
                      key={index}
                    >
                      {skill}
                    </span>

                  ))

                ) : (

                  <p>
                    No skills detected.
                  </p>

                )}

              </div>

            </div>


            {/* Experience */}

            <div className="profile-section">

              <h3>
                💼 Experience
              </h3>

              {profile.experience?.length > 0 ? (

                <ul>

                  {profile.experience.map(
                    (item, index) => (

                      <li key={index}>
                        {typeof item === "string"
                          ? item
                          : JSON.stringify(item)}
                      </li>

                    )
                  )}

                </ul>

              ) : (

                <p>
                  No experience detected.
                </p>

              )}

            </div>


            {/* Education */}

            <div className="profile-section">

              <h3>
                🎓 Education
              </h3>

              {profile.education?.length > 0 ? (

                <ul>

                  {profile.education.map(
                    (item, index) => (

                      <li key={index}>
                        {typeof item === "string"
                          ? item
                          : JSON.stringify(item)}
                      </li>

                    )
                  )}

                </ul>

              ) : (

                <p>
                  No education information detected.
                </p>

              )}

            </div>


            {/* Projects */}

            <div className="profile-section">

              <h3>
                🚀 Projects
              </h3>

              {profile.projects?.length > 0 ? (

                <ul>

                  {profile.projects.map(
                    (item, index) => (

                      <li key={index}>
                        {typeof item === "string"
                          ? item
                          : JSON.stringify(item)}
                      </li>

                    )
                  )}

                </ul>

              ) : (

                <p>
                  No projects detected.
                </p>

              )}

            </div>


            {/* Certifications */}

            <div className="profile-section">

              <h3>
                🏅 Certifications
              </h3>

              {profile.certifications?.length > 0 ? (

                <ul>

                  {profile.certifications.map(
                    (item, index) => (

                      <li key={index}>
                        {typeof item === "string"
                          ? item
                          : JSON.stringify(item)}
                      </li>

                    )
                  )}

                </ul>

              ) : (

                <p>
                  No certifications detected.
                </p>

              )}

            </div>


            {/* Languages */}

            <div className="profile-section">

              <h3>
                🌐 Languages
              </h3>

              {profile.languages?.length > 0 ? (

                <div className="tag-container">

                  {profile.languages.map(
                    (language, index) => (

                      <span
                        className="tag"
                        key={index}
                      >
                        {language}
                      </span>

                    )
                  )}

                </div>

              ) : (

                <p>
                  No languages detected.
                </p>

              )}

            </div>

          </section>

        )}

      </main>

    </div>
  );
}

export default App;