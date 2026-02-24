let scene, camera, renderer, controls;
let loader = new THREE.GLTFLoader();
let models = [];

// === SCENA ===
scene = new THREE.Scene();
scene.background = new THREE.Color(0xa5d9fd);

// FUNZIONE STAND
function createStand(x, z, color = 0x8e6bdc) {
const group = new THREE.Group();

const baseGeometry = new THREE.BoxGeometry(4, 0.5, 4);
const baseMaterial = new THREE.MeshStandardMaterial({ color });
const base = new THREE.Mesh(baseGeometry, baseMaterial);
base.position.y = 0.25;
base.castShadow = true;
base.receiveShadow = true;

const wallGeometry = new THREE.BoxGeometry(4, 3, 0.2);
const wallMaterial = new THREE.MeshStandardMaterial({ color: 0xffffff });
const wall = new THREE.Mesh(wallGeometry, wallMaterial);
wall.position.set(0, 1.75, -1.9);
wall.castShadow = true;

group.add(base);
group.add(wall);

group.position.set(x, 0, z);
scene.add(group);
}

// STAND DISPOSTI A GRIGLIA
const spacing = 7;
for (let x = -10; x <= 10; x += spacing) {
for (let z = -10; z <= 10; z += spacing) {
// createStand(x, z);
}
}


// LUCI
scene.add(new THREE.AmbientLight(0xffffff, 0.8));

const dirLight = new THREE.DirectionalLight(0xffffff, 0.6);
dirLight.position.set(5, 10, 0);
scene.add(dirLight);


// === CAMERA + RENDERER ===
const canvas = document.getElementById("room-canvas");
renderer = new THREE.WebGLRenderer({ canvas: canvas });
renderer.setSize(window.innerWidth, window.innerHeight);
let walkTime = 0;
let baseCameraHeight = 1.6;

camera = new THREE.PerspectiveCamera(
    65, window.innerWidth / window.innerHeight, 0.1, 1000
);

// === FOOTSTEP ===                                                                   CARICAMENTO SUONI !!!
let listener = new THREE.AudioListener();
camera.add(listener);

let stepSounds = [];
let audioLoader = new THREE.AudioLoader();

const stepFiles = [
    "/static/sounds/Step1.mp3",
    "/static/sounds/Step2.mp3",
    "/static/sounds/Step3.mp3",
    "/static/sounds/Step4.mp3",
    "/static/sounds/Step5.mp3",
    "/static/sounds/Step6.mp3",
    "/static/sounds/Step7.mp3",
    "/static/sounds/Step8.mp3",
];

stepFiles.forEach(file => {
    let sound = new THREE.Audio(listener);
    audioLoader.load(file, buffer => {
        sound.setBuffer(buffer);
        sound.setVolume(0.5);  // volume passi
    });
    stepSounds.push(sound);
});

// riprodurre un solo passo                                                            FUNZIONE SINGOLO PASSO !!!
function playStepSound() {
    if (stepSounds.length === 0) return;

    // prendi un suono random
    let snd = stepSounds[Math.floor(Math.random() * stepSounds.length)];

    // riproduci solo se non sta già suonando
    if (!snd.isPlaying) {
        snd.play();
    }
}

let stepTime = 0; // per footstep
// let isStepPlaying = false; // per footstep


// === CONTROLLI FPV ===
controls = new THREE.PointerLockControls(camera, document.body);
document.body.addEventListener("click", () => controls.lock());
camera.position.set(0, 1.6, 5);

// Movimento WASD
const velocity = new THREE.Vector3();
const direction = new THREE.Vector3();
const keys = {};
document.addEventListener("keydown", e => keys[e.code] = true);
document.addEventListener("keyup", e => keys[e.code] = false);

function movePlayer() {
    const speed = 0.1;
    direction.set(0, 0, 0);

    if (keys["KeyW"] || keys["ArrowUp"]) direction.z += 1;
    if (keys["KeyS"] || keys["ArrowDown"]) direction.z -= 1;
    if (keys["KeyA"] || keys["ArrowLeft"]) direction.x -= 1;
    if (keys["KeyD"] || keys["ArrowRight"]) direction.x += 1;

    let isMoving = direction.x !== 0 || direction.z !== 0;

    if (isMoving) {                                                                     // CONDIZIONE SUONO PASSI
        // tempo tra un passo e l'altro
        stepTime += 1;
        if (stepTime >= 25) { // più basso = passi più veloci                           // VELOCITà PASSI
            playStepSound();
            stepTime = 0;
        }
    } else {
        stepTime = 20; // reset quando ci si ferma
    }

    direction.normalize();
    velocity.copy(direction).multiplyScalar(speed);

    controls.moveRight(velocity.x);
    controls.moveForward(velocity.z);

    requestAnimationFrame(movePlayer);
}
movePlayer();

// === STANZA 3D ===
const floor = new THREE.Mesh(
    new THREE.PlaneGeometry(20, 20),
    new THREE.MeshStandardMaterial({ color: 0x808080 })
);
floor.rotation.x = -Math.PI / 2;
scene.add(floor);

function wall(x, z, rot = 0) {
    const wall = new THREE.Mesh(
        new THREE.BoxGeometry(20, 5, 0.2),
        new THREE.MeshStandardMaterial({ color: 0xaaaaaa })
    );
    wall.position.set(x, 2.5, z);
    wall.rotation.y = rot;
    scene.add(wall);
}
wall(0, -10);
wall(0, 10);
wall(-10, 0, Math.PI / 2);
wall(10, 0, Math.PI / 2);

// === CARICAMENTO MODELLI UTENTE ===
// window.MODELS_FROM_DJANGO.forEach(m => {
//     loader.load(m.url, gltf => {
//         const model = gltf.scene;
//         model.scale.set(m.scale, m.scale, m.scale);
//         model.position.set(m.pos[0], m.pos[1], m.pos[2]);
//         model.title.set(m.title, m.title, m.title);
//         scene.add(model);
//     });
// });

// === LOOP RENDER ===
function animate() {
    requestAnimationFrame(animate);
    // Effetto camminata (head bob)
    let isMoving =
        keys["KeyW"] || keys["KeyA"] || keys["KeyS"] || keys["KeyD"] ||
        keys["ArrowUp"] || keys["ArrowLeft"] || keys["ArrowDown"] || keys["ArrowRight"];

    if (isMoving) {
        walkTime += 0.25;  // velocità dell’oscillazione
        camera.position.y = baseCameraHeight + Math.sin(walkTime) * 0.08; // ampiezza oscillazione
    } else {
        // torna all'altezza normale quando fermo
        if (camera.position.y !== baseCameraHeight) {
            camera.position.y += (baseCameraHeight - camera.position.y) * 0.1;
        }
    };
    renderer.render(scene, camera);
}
animate();

// Resize dinamico
window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});


// window.addEventListener("DOMContentLoaded", () => {
//     setTimeout(() => {
//         document.getElementById("loading-screen").style.display = "none";
//     }, 1000);
// });

window.addEventListener("DOMContentLoaded", () => {
    setTimeout(hideLoading, 500); // 0.5 secondi per sparire schermata di caricamento
});

function hideLoading() {
    const screen = document.getElementById("loading-screen");
    if (!screen) return;

    // Aggiunge la classe hidden per iniziare il fade-out:
    screen.classList.add("hidden");

    // Dopo la durata della transizione, rimuove completamente l’elemento dal DOM:
    setTimeout(() => {
        screen.style.display = "none";
    }, 1000); // 1000ms = durata della transizione
}




// CODICE PER "FUNZIONAMENTO PUNTATORE A CROCE"

const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2(); // per click, ma qui è fisso al centro

// Oggetti su cui si può cliccare
const clickableObjects = []; // array in cui aggiungi i modelli dell’utente

// Aggiungi i modelli caricati dall’utente
window.MODELS_FROM_DJANGO.forEach(m => {
    loader.load(m.url, gltf => {
        const model = gltf.scene;
        model.scale.set(m.scale, m.scale, m.scale);
        model.position.set(m.pos[0], m.pos[1], m.pos[2]);
        //model.title.set(m.title, m.title, m.title);

        // Salva il titolo e la posizione dentro userData
        model.userData.title = m.title;
        model.userData.position = m.position;
        
        scene.add(model);
        clickableObjects.push(model);  // aggiungi al raycast
    });
});




// ===== POPUP al click degli oggetti =====

const popup = document.getElementById("object-popup");
const popupModelTitle = document.getElementById("popup-model-title");
const popupModelPosition = document.getElementById("popup-model-position");
const popupClose = document.getElementById("close-popup");

let popupOpen = false;

// CHIUSURA POPUP
popupClose.addEventListener("click", () => {
    popup.classList.add("hidden");
    popupOpen = false;

    // Riattiva PointerLock dopo un piccolo delay
    setTimeout(() => controls.lock(), 50);
});

// CLICK PER INTERAZIONE
window.addEventListener("click", () => {

    // Se popup aperto → ignora click e NON riapri altro
    if (popupOpen) return;

    // Se pointer lock non attivo → ignora
    if (!controls.isLocked) return;

    mouse.x = 0;
    mouse.y = 0;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(clickableObjects, true);

    if (intersects.length > 0) {
        let obj = intersects[0].object;

        // risali al parent principale del modello
        while (obj.parent && !obj.userData.title) {
            obj = obj.parent;
        }

        const title = obj.userData.title || "Titolo non disponibile";
        const positionText = obj.userData.position || "Posizione non disponibile";

        if (popupModelTitle) popupModelTitle.textContent = title;
        if (popupModelPosition) popupModelPosition.textContent = positionText;

        popup.classList.remove("hidden");
        popupOpen = true;

        // Interrompi subito il movimento della visuale
        controls.unlock();
    }
});

