import React from 'react';

class Display extends React.Component {
 constructor(props) {
   super(props);
 }

 callAPI() {
   return console.log("method called");
 }

 render() {
   return (
     <div className="row height400 bg-blue rounded-corners blk-border">
       <div>
         <div className="row bg-lt-gry height300 twelve columns column rounded-corners dropshadow">
           <p>This is the display frame</p>
         </div>
         <button className="button margin-30" onClick={this.callAPI}>
           This is a display selector
         </button>
         <button className="button margin-30" onClick={this.callAPI}>
           This is a display selector
         </button>
         <button className="button margin-30" onClick={this.callAPI}>
           This is a display selector
         </button>
       </div>
     </div>
   );
 }
}

export default Display
