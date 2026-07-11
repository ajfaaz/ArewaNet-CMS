function initBuilder() {
    const canvas = document.querySelector(".builder-canvas");
    const panel = document.getElementById("properties-panel");

    if (!canvas || !panel) {
        return;
    }

    let activeComponent = null;

    const setSelectedComponent = (component) => {
        canvas.querySelectorAll(".builder-component.selected").forEach((item) => {
            item.classList.remove("selected");
        });

        component.classList.add("selected");
        activeComponent = component;
    };

    const updatePreviewText = (selector, value) => {
        if (!activeComponent) {
            return;
        }

        const target = activeComponent.querySelector(selector);

        if (target) {
            target.textContent = value;
        }
    };

    const bindLivePreview = () => {
        const heading = document.getElementById("heading");
        const subheading = document.getElementById("subheading");
        const button = document.getElementById("button_text");

        if (heading) {
            heading.addEventListener("input", () => {
                updatePreviewText(".hero-heading", heading.value);
            });
        }

        if (subheading) {
            subheading.addEventListener("input", () => {
                updatePreviewText(".hero-subheading", subheading.value);
            });
        }

        if (button) {
            button.addEventListener("input", () => {
                updatePreviewText(".hero-button", button.value);
            });
        }
    };

    const renderProperties = async (component) => {
        panel.innerHTML = "<p>Loading properties...</p>";

        try {
            const response = await fetch(
                `/builder/api/component/${component.dataset.componentId}/`
            );

            if (!response.ok) {
                throw new Error("Failed to load component properties");
            }

            const data = await response.json();

            panel.innerHTML = `
                <h3>${data.type}</h3>

                <label for="heading">Heading</label>
                <input
                    id="heading"
                    type="text"
                    value="${data.heading || ""}"
                >

                <label for="subheading">Subheading</label>
                <textarea id="subheading">${data.subheading || ""}</textarea>

                <label for="button_text">Button Text</label>
                <input
                    id="button_text"
                    type="text"
                    value="${data.button_text || ""}"
                >
            `;

            bindLivePreview();
        } catch (error) {
            panel.innerHTML = `
                <div class="alert alert-danger">
                    Error loading properties: ${error.message}
                </div>
            `;
        }
    };

    canvas.addEventListener("click", (event) => {
        const component = event.target.closest(".builder-component");

        if (!component || !canvas.contains(component)) {
            return;
        }

        setSelectedComponent(component);
        renderProperties(component);
    });

    const firstComponent = canvas.querySelector(".builder-component");

    if (firstComponent) {
        setSelectedComponent(firstComponent);
        renderProperties(firstComponent);
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initBuilder);
} else {
    initBuilder();
}
