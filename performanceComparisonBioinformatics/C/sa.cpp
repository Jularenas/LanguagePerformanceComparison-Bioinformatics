#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <unordered_map>
#include <utility>
#include <algorithm>

#include <fstream>
#include <sstream>
using namespace std;

bool compare(std::pair<int,int> frst, std::pair<int,int> scnd) { return frst.second < scnd.second; }

std::vector<int> dc3(std::vector<int> arr)
{
	int original_size = arr.size();

	// B12_index: B1_index concatenate with B2_index = {1, 4, 7, ..., 2, 5, 8, ...}
	std::vector<int> B12_index;
	for (int i=0; i<original_size; i++)
		if (i%3 == 1)
			B12_index.push_back(i);
	for (int i=0; i<original_size; i++)
		if (i%3 == 2)
			B12_index.push_back(i);

	// insert 2 zero at the end of arr
	arr.push_back(0);
	arr.push_back(0);

	// store 3 succeding value as tuple for sorting B12
	// store index in B12.first
	// store tuple in B12.second
	std::vector<std::pair<int,int>> B12;
	int tuple;
	for (int i=0; i<B12_index.size(); i++)
	{
		tuple = arr.at(B12_index[i])*100 + arr.at(B12_index[i]+1)*10 + arr.at(B12_index[i]+2);
		B12.push_back(std::make_pair(B12_index[i], tuple));
	}

	// sort B12 
	// (we should use radix sort to acheive O(n) time,
	// but we will call sort() now for simplicity)
	sort(B12.begin(), B12.end(), compare);

	// store the rank
	std::vector<int> rank(arr.size(), 0);
	bool tie = false;
	for (int i=0; i<B12.size(); i++)
	{
		if (i == 0)
			rank[B12[0].first] = 1;
		else if (B12[i].second == B12[i-1].second)
		{
			tie = true;
			rank[B12[i].first] = rank[B12[i-1].first];
		}
		else
			rank[B12[i].first] = rank[B12[i-1].first] + 1;
	}
	
	// if tie, call dc3
	if (tie)
	{
		// store rank of B12
		std::vector<int> B12_rank;
		for (auto idx: B12_index)
			B12_rank.push_back(rank[idx]);

		// insert '$' at the end
		B12_rank.push_back(0);

		// call dc3 to resolve tie
		B12_rank = dc3(B12_rank);

		// update B12 to the new order
		// note: i starts from 1 to omit B12_rank[0] because it is '$'
		for (int i=1; i<B12_rank.size(); i++)
			B12.at(i-1).first = B12_index[B12_rank[i]];

		// update the rank
		for (int i=0; i<B12.size(); i++)
			rank[B12[i].first] = i+1;
	}
	
	// extract B0 pair
	std::vector<std::pair<int,int>> B0;
	for (int i=0; i<original_size; i++)
		if (i%3 == 0)
			B0.push_back(std::make_pair(i, arr[i]*10 + rank[i+1]));

	// sort B0 base on B12
	sort(B0.begin(), B0.end(), compare);

	// merge B0 and B12 
	std::vector<int> suffix_arr;
	int b0_index, b12_index, b0, b12;
	for (auto idx = std::make_pair(0, 0); idx.first < B0.size() || idx.second < B12.size();)
	{
		if (idx.first < B0.size() && idx.second < B12.size())
		{
			b0_index = B0[idx.first].first;
			b12_index = B12[idx.second].first;

			if (b12_index%3 == 1)
			{
				// B0 vs B1: rule 1
				b0 = arr[b0_index]*10 + rank[b0_index+1];
				b12 = arr[b12_index]*10 + rank[b12_index+1];
			}
			else 
			{
				// B0 vs B2: rule 2
				b0 = arr[b0_index]*100 + arr[b0_index+1]*10 + rank[b0_index+2];
				b12 = arr[b12_index]*100 + arr[b12_index+1]*10 + rank[b12_index+2];
			}

			if (b0 < b12)
			{
				suffix_arr.push_back(b0_index);
				idx.first++;
			}
			else
			{
				suffix_arr.push_back(b12_index);
				idx.second++;
			}
		}
		else if (idx.first < B0.size())
			for (; idx.first < B0.size(); idx.first++)
				suffix_arr.push_back(B0[idx.first].first);
		else 
			for (; idx.second < B12.size(); idx.second++)
				suffix_arr.push_back(B12[idx.second].first);

	}
	
	return suffix_arr;
}

int main(int argc, char** argv)
{
	string preFile1="fastaFiles/";
	preFile1+=argv[1];
	const char *f1 = preFile1.c_str();
    
	std::stringstream ss;
	string line;
	ifstream myfile (f1);
	if (myfile.is_open())
	{
		int i=0;
		while ( getline (myfile,line) )
		{
		  if(i==0){
		  		i++;	
			}
			else{
				ss << line ;
			}
		}
		myfile.close();
	}
	else cout << "Unable to open file"; 
	std::string s1 = ss.str();
	
	
	
	std::string str = s1;

	// calculate how many kinds of alphabet are there in the string
	std::set<char> alphabet;
	for (auto letter: str)
		alphabet.insert(letter);

	// rank alphabets
	std::unordered_map<char,int> alphabet_rank;
	for (auto i = std::make_pair(alphabet.begin(), 1); i.first != alphabet.end(); i.first++, i.second++)
		alphabet_rank[ *(i.first) ] = i.second;
	
	// replace letters in string with alphabet rank
	std::vector<int> new_str;
	for (auto letters: str)
		new_str.push_back( alphabet_rank[letters] );

	// insert '$' at the end
	new_str.push_back(0);
	str.push_back('$');

	// construct suffix array
	std::vector<int> suffix_arr;
	suffix_arr = dc3(new_str);

	// print result
	for (auto index: suffix_arr)
		std::cout << index << ": " << str.substr(index) << std::endl;

	return 0;
}
