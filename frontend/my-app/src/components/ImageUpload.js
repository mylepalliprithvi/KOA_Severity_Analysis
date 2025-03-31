import React, { useState } from 'react';
import axios from 'axios';

const ImageUpload = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [meanJointSpace, setMeanJointSpace] = useState('');
    const [severity,setSeverity] = useState('');
    const [treatmentPlan, setTreatmentPlan] = useState('');
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
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
            });

            console.log("Mean Joint Space: ", response.data.mean_joint_space);
            console.log("Severity : ",response.data.severity)

            if (response.data.mean_joint_space >= 0.35) {
                alert("Uploaded image is not a valid X-ray image. Please upload a valid X-ray image");
                return;
            } else 
                setMeanJointSpace(response.data.mean_joint_space);
                setSeverity(response.data.severity)
                setTreatmentPlan(getTreatmentPlan(response.data.severity));
        } catch (error) {
            console.error('Error uploading file:', error);
            alert("Can't upload file");
        }
    };

    // const handleTreatmentPlan = ()=> {
    //     alert(`Recommended Treatment for ${severity}:\n`+getTreatmentPlan(severity))
    // }

    const getTreatmentPlan = (severity) =>{
        switch(severity){
            case "Mild OA": return "Physical therapy, weight management, low-impact exercises"
            case "Moderate OA":
                return "Pain medications, joint braces, and physical therapy.";
            case "Severe OA":
                return "Consider surgery, joint replacement, and advanced pain management.";
            case "Healthy":
                return "No treatment needed."; 
            default:
                return "Consult a doctor for further evaluation";
        }
    };

    return (
        // <div>
        //     <input type="file" onChange={handleFileChange} />
        //     <button onClick={handleUpload}>Upload</button>
        //     {meanJointSpace && <div style={{ color: 'white' }}>Mean Joint Space : {meanJointSpace}</div>}
        //     {severity && <div style={{ color: 'white' }}>Severity: {severity}</div>}
        //     {severity && <button onClick={handleTreatmentPlan}>View Treatment Plan</button>}
        // </div>

<div className="container">
{/* File Upload Section */}
<div className="upload-section">
    <input type="file" onChange={handleFileChange} />
    <button onClick={handleUpload} className="upload-button">Upload</button>
</div>

{/* Display Results */}
{meanJointSpace && (
    <div className="result">
        <strong>Mean Joint Space:</strong> {meanJointSpace}
    </div>
)}
{severity && (
    <div className="result">
        <strong>Severity:</strong> {severity}
    </div>
)}

{/* Display Treatment Plan */}
{treatmentPlan && (
    <div className="treatment-plan">
        <strong>Treatment Plan:</strong> <br />
        {treatmentPlan}
    </div>
)}
</div>
    );
};

export default ImageUpload;


