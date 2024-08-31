document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('barGraph');
    const ctx = canvas.getContext('2d');

    const barWidth = 13;
    const barSpacing = 0;
    const barCount = 12;
    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;

    // Provided values for the bars
    const barValues = [500, 400, 600, 800, 100, 600, 400, 200, 250, 550, 560, 570];
    const incomeValues = [800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800, 800];

    // Calculate the maximum value to scale the bars
    const maxValue = Math.max(...barValues);

    // Function to scale bar heights
    const scaleHeight = (value) => (value / maxValue) * canvasHeight * 0.8; // 0.8 to leave some margin at the top

    // Draw gray bars
    for (let i = 0; i < barCount; i++) {
        const x = i * (barWidth + barSpacing) * 2; // Multiply by 2 for spacing the pairs
        const y = canvasHeight - scaleHeight(incomeValues[i]);
        const height = scaleHeight(incomeValues[i]);
        ctx.fillStyle = 'gray';
        ctx.fillRect(x, y, barWidth, height);
    }

    // Draw overlapping bars with linear gradient
    for (let i = 0; i < barCount; i++) {
        const x = i * (barWidth + barSpacing) * 2; // Multiply by 2 for spacing the pairs
        const y = canvasHeight - scaleHeight(barValues[i]);
        const height = scaleHeight(barValues[i]);
        const gradient = ctx.createLinearGradient(x, y, x, canvasHeight);
        gradient.addColorStop(0, '#C6F28F');
        gradient.addColorStop(1, '#BA8FF2');
        ctx.fillStyle = gradient;
        ctx.fillRect(x, y, barWidth, height);
    }
});
