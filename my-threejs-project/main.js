// Set up Three.js scene
const scene = new THREE.Scene();

// Set up camera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

// Set up renderer
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0xf1f1f1); // Set background color to light gray
document.getElementById('canvas-container').appendChild(renderer.domElement);

// Create a sphere geometry
const geometry = new THREE.SphereGeometry(1, 32, 32);

// Create a material
const material = new THREE.MeshStandardMaterial({
  color: 0xff0055,
  roughness: 0.5,
  metalness: 0.5
});

// Create a mesh and add it to the scene
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

// Set up ambient light
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

// Set up directional light
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(1, 1, 1).normalize();
scene.add(directionalLight);

// Raycaster for mouse interaction
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

// Show project details on click
document.addEventListener('click', onMouseClick, false);

function onMouseClick(event) {
  event.preventDefault();

  mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);

  const intersects = raycaster.intersectObjects(scene.children);

  if (intersects.length > 0) {
    const projectDetails = document.getElementById('project-details');
    projectDetails.style.display = 'block';
  }
}

// Render loop
function animate() {
  requestAnimationFrame(animate);

  // Rotate the sphere
  sphere.rotation.x += 0.01;
  sphere.rotation.y += 0.01;

  renderer.render(scene, camera);
}

animate();




