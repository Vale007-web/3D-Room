// import * as THREE from "https://cdnjs.cloudflare.com/ajax/libs/three.js/0.180.0/three.tsl.js";
// import { OrbitControls } from "jsm/controls/OrbitControls.js";

// // RENDERER
// const w = window.innerWidth;
// const h = window.innerHeight;
// const renderer = new THREE.WebGLRenderer({ antialias: true });
// renderer.setSize(w, h);
// document.body.appendChild(renderer.domElement);

// // CAMERA
// const fov = 75;
// const aspect = w / h;
// const near = 0.1;
// const far = 10;
// const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
// camera.position.z = 2;
// const scene = new THREE.Scene();

// const controls = new OrbitControls(camera, renderer.domElement);
// controls.enableDamping = true;
// controls.dampingFactor = 0.03;

// // CREAZIONE GEOMETRIA E MATERIALE, CREAZIONE MESH (GEO + MAT) E AGGIUNTA DELLA MESH ALLA SCENA 
// const geo = new THREE.IcosahedronGeometry(1.0, 2);
// const mat = new THREE.MeshStandardMaterial({ // Standard al posto del Basic per usare la luce
//     color: 0xffffff,
//     flatShading: true
// });
// const mesh =new THREE.Mesh(geo, mat);
// scene.add(mesh); // la mesh viene aggiunta alla scena come elemento figlio

// const wireMat = new THREE.MeshBasicMaterial({
//     color: 0xffffff,
//     wireframe: true
// });
// const wireMesh = new THREE.Mesh(geo, wireMat);
// wireMesh.scale.setScalar(1.001); // ingrandisce la wiremesh per evitare il flickering per sovrapposizione se con la stessa scala
// mesh.add(wireMesh); // la wiremesh è figlia della mesh principale, che a sua volta è figlia dell'intera scena

// // LUCE
// const hemiLight = new THREE.HemisphereLight(0x0099ff, 0xaa5500)
// scene.add(hemiLight);

// function animate(t = 0) {
//     console.log(t);
//     requestAnimationFrame(animate);
//     // mesh.scale.setScalar(Math.cos(t = 0.001) + 1.0);
//     mesh.rotation.y = t * 0.0001;
//     renderer.render(scene, camera);
//     controls.update();
// }
// animate();