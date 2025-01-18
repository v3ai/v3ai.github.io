document.addEventListener("DOMContentLoaded", () => {
  const contentDiv = document.getElementById("content");

  // Function to parse custom markup
  const parseMarkup = (markup) => {
    const lines = markup.split("\n");
    let flag = false;
    let html = "";

    lines.forEach((line) => {
      if (line.trim() === "") {
        html += "<br>";
      } else if (line.startsWith("---")) {
        if (!flag) {
          html += "<hr><ul>";
          flag = true;
        } else {
          html += "</ul><hr>";
          flag = false;
        }
      } else if (line.startsWith("-") && !line.startsWith("--")) {
        html += `<li>${line.slice(1).trim()}</li>`;
      } else {
        html += `<h3>${line.trim()}</h3>`;
      }
    });

    if (flag) {
      html += "</ul>"; // Close any unclosed list
    }

    return html;
  };

  // Cache-busting fetch utility
  const fetchWithCacheBust = (url) => {
    const cacheBustedUrl = `${url}?t=${new Date().getTime()}`;
    return fetch(cacheBustedUrl);
  };

  // Fetch the custom markup file
  fetchWithCacheBust("keys")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to load the markup file");
      }
      return response.text();
    })
    .then((markup) => {
      const parsedHTML = parseMarkup(markup);
      contentDiv.innerHTML = parsedHTML;
    })
    .catch((error) => {
      console.error("Error:", error);
      contentDiv.innerHTML = "<p>Failed to load content.</p>";
    });
});
