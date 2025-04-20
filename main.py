from app import create_app

app = create_app()

with app.test_client() as client:
        # Simulate a form submission via POST request
        response = client.post('/', data={
            'age_group': '31-40',
            'profession': 'Engineer',
            'lifestyle': 'Professional',
            'personality': 'Analytical',
            'design': 'Classic',
            'price_range': 'Luxury',
            'material': 'Gold',
            'functionality': 'Durability'
        })
        
        if response.status_code == 200:
            print("Test Passed: Form submission successful")
        else:
            print(f"Test Failed: Form submission failed with status code {response.status_code}")

if __name__ == '__main__':
    app.run(debug=True)
