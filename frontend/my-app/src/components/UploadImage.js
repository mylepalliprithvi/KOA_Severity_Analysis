import React from "react";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faUpload} from '@fortawesome/free-solid-svg-icons';
import { useState } from 'react';
import axios from "axios";
const UploadImage = () => {
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
                    'Acess-Control-Allow-Origin':'http://localhost:3000'
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
            <FontAwesomeIcon icon="fa-solid fa-cloud-arrow-up" onClick={handleUpload}/>
            <button onClick={handleUpload}>Upload</button>
            {meanJointSpace && <div>Mean Joint Space : {meanJointSpace}</div>}
        </div>
    );
};

export default UploadImage;
