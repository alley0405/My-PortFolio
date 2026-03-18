import re

new_script = """    let state = {
      hoveredNodeId: null,
      rotationAngle: 0,
      pulseEffect: {},
      centerOffset: { x: 0, y: 0 },
      domNodes: {}
    };

    const container = document.getElementById('container');
    const nodesContainer = document.getElementById('nodes-container');

    const getStatusStyles = (status) => {
      switch (status) {
        case "completed": return "text-white bg-black border-white";
        case "in-progress": return "text-black bg-white border-black";
        case "pending": return "text-white bg-black/40 border-white/50";
        default: return "text-white bg-black/40 border-white/50";
      }
    };

    const getRelatedItems = (itemId) => {
      const item = timelineData.find(i => i.id === itemId);
      return item ? item.relatedIds : [];
    };

    const calculateNodePosition = (index, total) => {
      const angle = ((index / total) * 360 + state.rotationAngle) % 360;
      const radius = 220;
      const radian = (angle * Math.PI) / 180;
      const x = radius * Math.cos(radian) + state.centerOffset.x;
      const y = radius * Math.sin(radian) + state.centerOffset.y;
      const zIndex = Math.round(100 + 50 * Math.cos(radian));
      // Ensure opacity minimum for legibility when behind
      const opacity = Math.max(0.4, Math.min(1, 0.4 + 0.6 * ((1 + Math.sin(radian)) / 2)));
      return { x, y, angle, zIndex, opacity };
    };

    const handleHover = (id) => {
      state.hoveredNodeId = id;
      state.pulseEffect = {};
      const related = getRelatedItems(id);
      related.forEach(relId => { state.pulseEffect[relId] = true; });
      updateNodes();
    };

    const handleMouseLeave = () => {
      state.hoveredNodeId = null;
      state.pulseEffect = {};
      updateNodes();
    };

    window.scrollToNode = (id) => {
      handleHover(id);
    };

    const initNodes = () => {
      nodesContainer.innerHTML = '';
      
      timelineData.forEach((item, index) => {
        const wrapper = document.createElement('div');
        wrapper.className = 'absolute transition-all duration-300 node-item';
        // Base coordinate placement
        wrapper.style.cssText = `
           left: 50%; top: 50%;
           margin-left: -20px; margin-top: -20px;
        `;
        
        wrapper.onmouseenter = () => handleHover(item.id);
        wrapper.onmouseleave = () => handleMouseLeave();

        const energyBg = document.createElement('div');
        energyBg.className = 'energy-bg absolute rounded-full -inset-1';
        energyBg.style.background = `radial-gradient(circle, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 70%)`;
        const size = item.energy * 0.5 + 40;
        energyBg.style.width = `${size}px`;
        energyBg.style.height = `${size}px`;
        energyBg.style.left = `-${(size - 40) / 2}px`;
        energyBg.style.top = `-${(size - 40) / 2}px`;
        wrapper.appendChild(energyBg);

        const nodeCircle = document.createElement('div');
        nodeCircle.className = 'node-circle w-10 h-10 rounded-full flex items-center justify-center border-2 transition-all duration-300 transform cursor-pointer';
        nodeCircle.innerHTML = `<i data-lucide="${item.icon}" style="width: 16px; height: 16px;"></i>`;
        wrapper.appendChild(nodeCircle);

        const nodeTitle = document.createElement('div');
        nodeTitle.className = 'node-title absolute top-12 left-1/2 -translate-x-1/2 whitespace-nowrap text-xs font-semibold tracking-wider transition-all duration-300';
        nodeTitle.innerText = item.title;
        wrapper.appendChild(nodeTitle);

        const card = document.createElement('div');
        // We set scale-0 opacity-0 pointer-events-none by default
        card.className = "node-card absolute top-24 left-1/2 -translate-x-1/2 w-64 bg-black/95 backdrop-blur-xl border border-white/30 rounded-lg shadow-2xl shadow-white/20 overflow-visible text-left z-50 transition-all duration-500 scale-0 opacity-0 pointer-events-none transform origin-top";
        
        // Ensure card can be hovered recursively
        card.onmouseenter = () => handleHover(item.id);
        
        let relatedButtonsHtml = '';
        if (item.relatedIds.length > 0) {
          relatedButtonsHtml = `
            <div class="mt-4 pt-3 border-t border-white/10">
              <div class="flex items-center mb-2 text-white/70">
                <i data-lucide="link" style="width:10px; height:10px; margin-right:4px;"></i>
                <h4 class="text-[10px] uppercase tracking-wider font-medium">Connected Nodes</h4>
              </div>
              <div class="flex flex-wrap gap-1">
                ${item.relatedIds.map(rId => {
                  const rItem = timelineData.find(i => i.id === rId);
                  return `<button class="related-btn flex items-center h-6 px-2 py-0 text-[10px] rounded border border-white/20 bg-transparent hover:bg-white/10 text-white/80 hover:text-white transition-all cursor-pointer" onclick="window.scrollToNode(${rId})">
                    ${rItem?.title} <i data-lucide="arrow-right" style="width:8px; height:8px; margin-left:4px;"></i>
                  </button>`;
                }).join('')}
              </div>
            </div>
          `;
        }

        card.innerHTML = `
          <div class="absolute -top-3 left-1/2 -translate-x-1/2 w-px h-3 bg-white/50"></div>
          <div class="p-4 pb-2 border-b border-white/10">
            <div class="flex justify-between items-center text-xs mb-2">
              <span class="inline-flex items-center rounded-full border px-2 py-0.5 text-[9px] font-bold ${getStatusStyles(item.status)}">
                 ${item.status === 'completed' ? 'COMPLETE' : item.status === 'in-progress' ? 'IN PROGRESS' : 'PENDING'}
              </span>
              <span class="font-mono text-white/50 text-[10px]">${item.date}</span>
            </div>
            <h3 class="text-sm font-bold m-0 leading-none">${item.title}</h3>
          </div>
          <div class="p-4 pt-3 text-xs text-white/80">
            <p class="m-0 mb-3 leading-relaxed">${item.content}</p>
            
            <div class="mt-2 text-[10px] space-y-2 border-t border-white/10 pt-2">
              ${item.qualities ? item.qualities.map(q => `
                <div>
                  <div class="flex justify-between items-center mb-1">
                    <span class="text-white/80 tracking-wide">${q.name}</span>
                    <span class="font-mono text-white/60">${q.val}/100</span>
                  </div>
                  <div class="w-full h-[3px] bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-white/80 transition-all duration-1000 ease-out fill-bar" style="width: 0%;" data-w="${q.val}%"></div>
                  </div>
                </div>
              `).join('') : ''}
            </div>

            <div class="mt-3 pt-3 border-t border-white/10">
              <div class="flex justify-between items-center text-[10px] mb-1">
                <span class="flex items-center text-white/90">
                  <i data-lucide="zap" style="width:10px; height:10px; margin-right:4px; color: #eab308;"></i> Energy Level
                </span>
                <span class="font-mono font-bold">${item.energy}%</span>
              </div>
              <div class="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                <div class="h-full bg-gradient-to-r from-blue-500 to-purple-500" style="width: ${item.energy}%"></div>
              </div>
            </div>
            ${relatedButtonsHtml}
          </div>
        `;
        wrapper.appendChild(card);
        nodesContainer.appendChild(wrapper);

        state.domNodes[item.id] = { wrapper, energyBg, nodeCircle, nodeTitle, card };
      });

      if (typeof lucide !== 'undefined') {
        lucide.createIcons();
      }
    };

    const updateNodes = () => {
      timelineData.forEach((item, index) => {
        const position = calculateNodePosition(index, timelineData.length);
        const dom = state.domNodes[item.id];
        if (!dom) return;
        
        const isHovered = (state.hoveredNodeId === item.id);
        const isRelated = state.hoveredNodeId && getRelatedItems(state.hoveredNodeId).includes(item.id);
        const isPulsing = !!state.pulseEffect[item.id];
        
        // Cache positions so that hover and rotation apply smoothly together
        dom.wrapper.style.transform = `translate(${position.x}px, ${position.y}px)`;
        dom.wrapper.style.zIndex = isHovered ? 300 : position.zIndex;
        dom.wrapper.style.opacity = isHovered ? 1 : position.opacity;

        if (isPulsing) {
            dom.energyBg.classList.add('animate-pulse', 'duration-1000');
        } else {
            dom.energyBg.classList.remove('animate-pulse', 'duration-1000');
        }

        let circleClasses = 'node-circle w-10 h-10 rounded-full flex items-center justify-center border-2 transition-all duration-300 transform ';
        if (isHovered) {
          circleClasses += 'bg-white text-black border-white shadow-lg shadow-white/30 scale-150 relative z-20';
        } else if (isRelated) {
          circleClasses += 'bg-white/50 text-black border-white animate-pulse';
        } else {
          circleClasses += 'bg-black text-white border-white/40';
        }
        dom.nodeCircle.className = circleClasses;

        let titleClasses = 'node-title absolute top-12 left-1/2 -translate-x-1/2 whitespace-nowrap text-xs font-semibold tracking-wider transition-all duration-300 ';
        if (isHovered) {
            titleClasses += 'text-white scale-125 top-16 z-20';
        } else {
            titleClasses += 'text-white/70';
        }
        dom.nodeTitle.className = titleClasses;

        if (isHovered) {
            dom.card.classList.remove('scale-0', 'opacity-0', 'pointer-events-none');
            dom.card.classList.add('scale-100', 'opacity-100', 'pointer-events-auto');
            
            // Reflow width bars
            setTimeout(() => {
                const bars = dom.card.querySelectorAll('.fill-bar');
                bars.forEach(bar => {
                  bar.style.width = bar.getAttribute('data-w');
                });
            }, 50);
        } else {
            dom.card.classList.add('scale-0', 'opacity-0', 'pointer-events-none');
            dom.card.classList.remove('scale-100', 'opacity-100', 'pointer-events-auto');
            const bars = dom.card.querySelectorAll('.fill-bar');
            bars.forEach(bar => {
              bar.style.width = '0%';
            });
        }
      });
    };

    let lastTime = 0;
    const rotateLoop = (timestamp) => {
      if (!lastTime) lastTime = timestamp;
      const progress = timestamp - lastTime;
      
      // Update rotation consistently (rotation shouldn't stop!)
      if (progress > 50) { 
        state.rotationAngle = Number(((state.rotationAngle + 0.15) % 360).toFixed(3));
        updateNodes();
        lastTime = timestamp;
      }
      
      requestAnimationFrame(rotateLoop);
    };

    initNodes();
    requestAnimationFrame(rotateLoop);
"""

with open('skills.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Regex to match from `let state = {` up to `requestAnimationFrame(rotateLoop);`
pattern = re.compile(r'    let state = \{.*?requestAnimationFrame\(rotateLoop\);', re.DOTALL)

# verify we found it
match = pattern.search(content)
if not match:
    print("Pattern not found!")
else:
    new_content = pattern.sub(new_script, content)
    with open('skills.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success replacing!")
