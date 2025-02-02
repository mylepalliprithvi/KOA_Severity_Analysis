// src/App.js
import React from 'react';
import ImageUpload from './components/ImageUpload';
import UploadImage from './components/UploadImage';

const App = () => {
    return (
        <div>
            <h1>Knee Osteoarthritis Severity Prediction</h1>
            <UploadImage/>
           {/* <ImageUpload />*/}
        </div>
    );
};

export default App;
