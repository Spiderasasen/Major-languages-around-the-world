import {useState, useEffect} from 'react'

function Home(){
    return(
        <div>
            <h1>Major Languages from Around the World</h1>
            <h3>Please chose 1 of the 3 options</h3>
            <div>
                <li>Search via Continent</li>
                <li>Search via Category</li>
                <li>Look at all Languages</li>
            </div>
        </div>
    );
}
export default Home;