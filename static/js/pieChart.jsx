import React from "react";

class pieChart extends React.Component {
  render() {
    
    const {props} = this, {width, height, data} = props;
    const radius = Math.min(width, height) / 2;
    const layout = d3.pie()(data);
    const arcGen = d3.arc()
      .innerRadius(radius * 0.2)
      .outerRadius(radius * 0.9);
    const color = d3.scaleOrdinal(d3.schemeCategory10);
    
    return (
      <svg {...props}>
      <g transform={`translate(${width/2},${height/2})`}>
        {layout.map((d, i) => {
          return <path d={arcGen(d)} key={i} style={{fill: color(i)}}/>
        })}
      </g>
    </svg>
      )
  }
}

export default pieChart