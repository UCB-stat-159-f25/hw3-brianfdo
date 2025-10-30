from ligotools.utils import whiten, write_wavfile, reqshift, make_the_plots
import numpy as np
from scipy.io import wavfile

def test_whiten_function():
    """Test basic functionality of whiten"""
    sample_rate = 4096
    dt = 1.0 / sample_rate
    t = np.linspace(0, 1.0, sample_rate)
    frequency = 100
    test_signal = np.sin(2 * np.pi * frequency * t) + 0.1 * np.random.normal(size=len(t))

    # create my own psd function
    def my_psd(freqs):
        return np.ones_like(freqs) * 1e-46
    
    try:
        whitened_signal = whiten(test_signal, my_psd, dt)
        assert whitened_signal.shape == test_signal.shape
        assert not np.allclose(whitened_signal, test_signal)
    except Exception as e:
        assert False

def test_reqshift_function():
    """Test basic functionality of reqshift"""
    sample_rate = 4096
    dt = 1.0 / sample_rate
    t = np.linspace(0, 1.0, sample_rate)
    frequency = 100
    test_signal = np.sin(2 * np.pi * frequency * t) + 0.1 * np.random.normal(size=len(t))
    
    try:
        shifted_signal = reqshift(test_signal, fshift=200, sample_rate=sample_rate)
        assert shifted_signal.shape == test_signal.shape
    except Exception as e:
        assert False
        
def test_write_wav_function():
    try:
        sample_rate = 4096
        t = np.linspace(0, 1.0, sample_rate)
        audio_signal = np.sin(2 * np.pi * 100 * t)
        write_wavfile('test_audio.wav', sample_rate, audio_signal)
        
        # Verify the file was created and can be read
        fs_read, data_read = wavfile.read('audio/test_audio.wav')
        assert fs_read == sample_rate
        assert len(data_read) == len(audio_signal)
        
        import os
        os.remove('audio/test_audio.wav')
        
    except Exception as e:
        assert False
