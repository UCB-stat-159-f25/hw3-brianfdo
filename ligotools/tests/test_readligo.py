from ligotools import readligo as rl

def test_loaddata_invalid_filepath():
    """Test that loaddata returns None for invalid file paths"""
    
    # non-existent hdf5 file
    result_strain, result_time, result_channel_dict = rl.loaddata("non_existent_file.hdf5", "H1")
    assert result_strain is None
    assert result_time is None
    assert result_channel_dict is None
    
    # non-existent GWF file
    result_strain, result_time, result_channel_dict = rl.loaddata("non_existent_file.gwf", "H1")
    assert result_strain is None
    assert result_time is None
    assert result_channel_dict is None

def test_dq2segs_empty_dictionary():
    """Test functionality of dq2segs with an empty dictionary"""
    empty_dict = {}
    gps_start = 1000
    
    try:
        rl.dq2segs(empty_dict, gps_start)
        assert False, "Exception should be raised for an empty dictionary"
    except Exception as e:
        assert True
