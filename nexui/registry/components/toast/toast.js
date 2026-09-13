// NexUI Toast v1.0.0
// Load this script BEFORE Alpine.js initializes.
document.addEventListener("alpine:init", () => {
  Alpine.data("nexuiToast", () => ({
    toasts: [],

    show({ title, description = "", variant = "default", duration = 4000 }) {
      const id = Date.now() + Math.random();
      this.toasts.push({ id, title, description, variant, visible: true });
      setTimeout(() => this.remove(id), duration);
    },

    remove(id) {
      const toast = this.toasts.find((t) => t.id === id);
      if (toast) toast.visible = false;
      setTimeout(() => {
        this.toasts = this.toasts.filter((t) => t.id !== id);
      }, 300);
    },
  }));
});
