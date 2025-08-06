function activateClientZone(zoneId) {
    const zones = ['zone2', 'zone3'];
    zones.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.style.display = (id === zoneId) ? 'block' : 'none';
        }
    });
}