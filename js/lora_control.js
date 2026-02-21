/**
 * Comfy-Lora-Control - JavaScript Extensions
 * 
 * This file contains frontend extensions for the ComfyUI interface.
 * Add custom widgets, UI modifications, or client-side logic here.
 */

import { app } from "../../scripts/app.js";

// Extension registration
app.registerExtension({
    name: "Comfy.LoraControl",
    
    async setup() {
        console.log("[Comfy-Lora-Control] Extension loaded");
    },
    
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        // Customize node registration here if needed
    },
    
    async nodeCreated(node) {
        // Called when a node is created
        // Add custom behavior for your nodes here
    },
    
    async loadedGraphNode(node) {
        // Called when a node is loaded from a workflow
    }
});

console.log("[Comfy-Lora-Control] JavaScript module initialized");
