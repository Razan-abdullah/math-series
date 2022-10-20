import pytest

from series import fibonacci,lucas


# @pytest.mark.skip("pending")
def test_fibonacci():
    actual = fibonacci(0)
    expected =[]
    assert actual == expected
    
# @pytest.mark.skip("pending")  
def test_fibonacci():
    actual = fibonacci(1)
    expected =[0]
    assert actual == expected
    
# @pytest.mark.skip("pending")
def test_fibonacci():
    actual = fibonacci(2)
    expected = [0,1]
    assert actual == expected



# @pytest.mark.skip("pending")    
def test_fibonacci():
    actual = fibonacci(3)
    expected = [0,1,1]
    assert actual == expected
    
    
# @pytest.mark.skip("pending")    
def test_fibonacci():
    actual = fibonacci(4)
    expected = [0,1,1,2]
    assert actual == expected        
    
    
    
    
    
# @pytest.mark.skip("pending")    
def test_lucas():
    actual = lucas(0)
    expected =[]
    assert actual == expected
    
    
    
# @pytest.mark.skip("pending")    
def test_lucas():
    actual = lucas(1)
    expected =[2]
    assert actual == expected    



# @pytest.mark.skip("pending")    
def test_lucas():
    actual = lucas(2)
    expected =[2,1]
    assert actual == expected  

# @pytest.mark.skip("pending")
def test_lucas():
    actual = lucas(3)
    expected =[2,1,3]
    assert actual == expected 
    
    
# @pytest.mark.skip("pending")    
def test_lucas():
    actual = lucas(4)
    expected =[2,1,3,4]
    assert actual == expected         
    
    
# @pytest.mark.skip("pending")    
def test_sum():
    actual = sum(lucas(4))
    expected =10
    assert actual == expected 
    
# @pytest.mark.skip("pending")    
def test_sum():
    actual = sum(fibonacci(5))
    expected =7
    assert actual == expected             
    

    
    
    
    

    
   
    

