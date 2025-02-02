import React, { useState } from 'react';
import axios from 'axios';

const ImageUpload = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    //const [severity, setSeverity] = useState('');
    const [meanJointSpace,setMeanJointSpace] = useState('');
    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await axios.post('http://localhost:5000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            //setSeverity(response.data.severity); 
            setMeanJointSpace(response.data.mean_joint_space);
            //console.log(response.data.severity)
            console.log("Mean joint space: ",response.data.mean_joint_space)// Capture the severity results
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            {meanJointSpace && <div>Mean Joint Space : {meanJointSpace}</div>}
        </div>
    );
};

export default ImageUpload;

