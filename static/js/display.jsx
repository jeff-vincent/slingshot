import React from 'react';

import pieChart from './pieChart'

class Display extends React.Component {
 constructor(props) {
   super(props);
 }

 callAPI() {
   return render_template('sign-up.html');
 }

 render() {
   return (
     <div className="row height400 bg-blue rounded-corners blk-border">
       <div>
         <div className="row bg-lt-gry height300 twelve columns column rounded-corners dropshadow">
           <pieChart width={100} height={100} data={[1,2,8]} />
           <pieChart width={100} height={100} data={[4,1,6]} />
           <pieChart width={100} height={100} data={[1,6,7]} />
         </div>
         <button className="button margin-30" onClick={this.callAPI}>
           Update
         </button>
       </div>
     </div>
   );
 }
}

export default Display
