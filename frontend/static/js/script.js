(() => {

  const form = document.getElementById("personForm");

  if (form) {

    const notice = document.getElementById("notice");
    const button = form.querySelector('button[type="submit"]');

    function showMessage(message, type) {
      notice.textContent = message;
      notice.className = `notice ${type}`;
      notice.hidden = false;
    }

    form.addEventListener("submit", async (event) => {

      event.preventDefault();

      if (!form.reportValidity()) {
        return;
      }

      const data = Object.fromEntries(
        new FormData(form).entries()
      );

      data.person_name = data.person_name.trim();
      data.mobile_number = data.mobile_number.trim();
      data.city = data.city.trim();
      data.state = data.state.trim();
      data.post_code = data.post_code.trim();
      data.full_address = data.full_address.trim();

      data.age = Number(data.age);

      if (!/^[A-Za-z][A-Za-z '-]*$/.test(data.person_name)) {
        showMessage(
          "Name can contain only letters, spaces, hyphens and apostrophes.",
          "error"
        );
        return;
      }

      if (!/^\+?\d{10,15}$/.test(data.mobile_number)) {
        showMessage("Please enter a valid mobile number.", "error");
        return;
      }

      if (data.age < 1 || data.age > 120) {
        showMessage("Age must be between 1 and 120.", "error");
        return;
      }

      if (!data.city || !data.state || !data.post_code || !data.full_address) {
        showMessage("Please fill all required fields.", "error");
        return;
      }

      try {

        button.disabled = true;
        button.textContent = "Saving...";

        const response = await fetch("/api/persons/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
          },
          body: JSON.stringify(data)
        });

        const result = await response.json();

        if (!response.ok) {
          if (result.person_name) {
            showMessage("Person Name Validation: " + result.person_name[0], "error");
            return;
          }

          if (result.mobile_number) {
            showMessage("Mobile Number Validation: " + result.mobile_number[0], "error");
            return;
          }

          if (result.age) {
            showMessage("Age Validation: " + result.age[0], "error");
            return;
          }

          if (result.city) {
            showMessage("City Validation: " + result.city[0], "error");
            return;
          }

          if (result.state) {
            showMessage("State Validation: " + result.state[0], "error");
            return;
          }

          if (result.post_code) {
            showMessage("Post Code Validation: " + result.post_code[0], "error");
            return;
          }

          if (result.full_address) {
            showMessage("Address Validation: " + result.full_address[0], "error");
            return;
          }

          showMessage("Unable to save the record.", "error");
          return;
        }

        form.reset();

        showMessage(
          "Person saved successfully.",
          "success"
        );

      } catch (error) {

        showMessage(
          "Unable to connect to the server.",
          "error"
        );

      } finally {

        button.disabled = false;
        button.textContent = "Save Person";
      }
    });
  }

  const rows = document.getElementById("personRows");

  if (rows) {

    const count = document.getElementById("recordCount");
    const notice = document.getElementById("listNotice");

    async function loadPeople() {

      try {

        const response = await fetch("/api/persons/");

        if (!response.ok) {
          throw new Error("Unable to load records.");
        }

        const people = await response.json();

        count.textContent = `${people.length} records`;

        rows.replaceChildren();

        if (people.length === 0) {

          const row = document.createElement("tr");
          const cell = document.createElement("td");

          cell.colSpan = 7;
          cell.textContent = "No records found.";

          row.appendChild(cell);
          rows.appendChild(row);

          return;
        }

        people.forEach(person => {

          const row = document.createElement("tr");

          const fields = [
            person.person_name,
            person.mobile_number,
            person.age,
            person.city,
            person.state,
            person.post_code,
            person.full_address
          ];

          fields.forEach(value => {

            const cell = document.createElement("td");

            cell.textContent = value;

            row.appendChild(cell);
          });

          rows.appendChild(row);
        });

      } catch (error) {

        notice.textContent = error.message;
        notice.className = "notice error";
        notice.hidden = false;
      }
    }

    loadPeople();
  }

})();