package com.example.portalulinstanelor.ui.home;

import static com.android.volley.toolbox.Volley.newRequestQueue;

import android.util.Log;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import java.io.IOException;

public class HomeViewModel extends ViewModel {

    private MutableLiveData<String> mText;

    public HomeViewModel() throws IOException {
        mText = new MutableLiveData<>();

        mText.setValue("This is home fragment");
        Log.d("HomeView", "Test message");

    }

    public LiveData<String> getText() {
        return mText;
    }
}