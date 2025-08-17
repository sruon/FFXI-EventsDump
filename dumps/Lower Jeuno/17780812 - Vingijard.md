# 17780812 - Vingijard

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 380 bytes             |
| Total Events     | 2                     |
| References Count | 23                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10034](#event-10034) | 0x0001       |    263 |             61 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2710      |       10000 |
|       1 | 0x2177      |        8567 |
|       2 | 0xFFFFFFFE  |  4294967294 |
|       3 | 0x40000000  |  1073741824 |
|       4 | 0x2178      |        8568 |
|       5 | 0x2179      |        8569 |
|       6 | 0x217A      |        8570 |
|       7 | 0x217B      |        8571 |
|       8 | 0x217C      |        8572 |
|       9 | 0x217D      |        8573 |
|      10 | 0x217E      |        8574 |
|      11 | 0x217F      |        8575 |
|      12 | 0x2180      |        8576 |
|      13 | 0x2181      |        8577 |
|      14 | 0x0000      |           0 |
|      15 | 0x2182      |        8578 |
|      16 | 0x2183      |        8579 |
|      17 | 0x2184      |        8580 |
|      18 | 0x00FD      |         253 |
|      19 | 0x2185      |        8581 |
|      20 | 0x0078      |         120 |
|      21 | 0x00C8      |         200 |
|      22 | 0x00B4      |         180 |

## String References

- **8577**: Which memory do you wish to relive? [I have changed my mind./The warrior artifact quests./The monk artifact quests./The white mage artifact quests./The black mage artifact quests./The red mage artifact quests./The thief artifact quests./The paladin artifact quests./The dark knight artifact quests./The beastmaster artifact quests./The bard artifact quests./The ranger artifact quests./The samurai artifact quests./The ninja artifact quests./The dragoon artifact quests./The summoner artifact quests./The blue mage artifact quests./The corsair artifact quests./The puppetmaster artifact quests./The dancer artifact quests./The scholar artifact quests./The geomancer artifact quests./The rune fencer artifact quests.]
- **8580**: Have your memories erased? [I need more time to think./I have made up my mind.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 10034

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 263 bytes |
| Instructions | 59        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 09 10 00 80 1E F0  FF FF 7F 2B 4C 50 0F 01   ..........+LP..
0010: 01 80 23 02 02 10 02 80  00 22 00 03 01 10 03 80  ..#......"......
0020: 21 00 2B 4C 50 0F 01 04  80 23 2B 4C 50 0F 01 05  !.+LP....#+LP...
0030: 80 23 2B 4C 50 0F 01 06  80 23 2B 4C 50 0F 01 07  .#+LP....#+LP...
0040: 80 23 2B 4C 50 0F 01 08  80 23 02 03 10 09 10 03  .#+LP....#......
0050: 61 00 2B 4C 50 0F 01 09  80 23 03 01 10 03 80 21  a.+LP....#.....!
0060: 00 2B 4C 50 0F 01 0A 80  23 2B 4C 50 0F 01 0B 80  .+LP....#+LP....
0070: 23 2B 4C 50 0F 01 0C 80  23 24 0D 80 0E 80 02 10  #+LP....#$......
0080: 25 02 00 10 0E 80 00 93  00 03 01 10 03 80 21 00  %.............!.
0090: 01 93 00 03 01 10 00 10  2B 4C 50 0F 01 0F 80 23  ........+LP....#
00A0: 2B 4C 50 0F 01 0B 80 23  2B 4C 50 0F 01 10 80 23  +LP....#+LP....#
00B0: 24 11 80 0E 80 0E 80 25  02 00 10 0E 80 00 CA 00  $......%........
00C0: 03 01 10 03 80 21 00 01  CA 00 42 73 12 80 F8 FF  .....!....Bs....
00D0: FF 7F F0 FF FF 7F 2B 4C  50 0F 01 13 80 1C 14 80  ......+LP.......
00E0: 45 15 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 32 0E  E..........fdo2.
00F0: 80 1C 16 80 23 45 15 80  F0 FF FF 7F F0 FF FF 7F  ....#E..........
0100: 66 64 69 32 0E 80 21 00                           fdi2..!.        
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[9] = 10000*
  1: 0x0006 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000B [0x2B] Vingijard (ID: 17780812/0x010F504C) [8567*]:
    → "Memories new are often born from those forgotten..."
  3: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0013 [0x02] IF !(Work_Zone[2] == 4294967294*) GOTO 0x0022
  5: 0x001B [0x03] Work_Zone[1] = 1073741824*
  6: 0x0020 [0x21] END_EVENT
  7: 0x0021 [0x00] END_REQSTACK()
  8: 0x0022 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8568*]:
    → "The easiest way to relive your past is to first cleanse your mind of it."
  9: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002A [0x2B] Vingijard (ID: 17780812/0x010F504C) [8569*]:
    → "I can assist you in the task of erasing the annals inscribed deep within your soul."
 11: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0032 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8570*]:
    → "...And with this, give you the opportunity to rewrite your history anew."
 13: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003A [0x2B] Vingijard (ID: 17780812/0x010F504C) [8571*]:
    → "Of course, this path, if you choose to tread it, will not be simple."
 15: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0042 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8572*]:
    → "For a donation of $7 gil, I will wipe clean your heart of three or four quests, allowing you to once again experience the hardships, the tribulations, and the joy that accompany them."
 17: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x004A [0x02] IF !(Work_Zone[3] >= Work_Zone[9]) GOTO 0x0061
 19: 0x0052 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8573*]:
    → "However, it seems your purse is too light. Return again when fortune has smiled upon you."
 20: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x005A [0x03] Work_Zone[1] = 1073741824*
 22: 0x005F [0x21] END_EVENT
 23: 0x0060 [0x00] END_REQSTACK()
 24: 0x0061 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8574*]:
    → "Just as when you first completed them, you will be able to reap the rewards that await you when completing the tasks."
 25: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0069 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8575*]:
    → "However, there are items that fate will not allow you to possess more than one of. If you wish to obtain these items again, you must first cast away those that you still hold on to."
 27: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0071 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8576*]:
    → "Now it is time for you to choose..."
 29: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0079 [0x24] CREATE_DIALOG(message_id=8577*, default_option=0*, option_flags=Work_Zone[2])
    → "Which memory do you wish to relive? [I have changed my mind./The warrior artifact quests./The monk artifact quests./The white mage artifact quests./The black mage artifact quests./The red mage artifact quests./The thief artifact quests./The paladin artifact quests./The dark knight artifact quests./The beastmaster artifact quests./The bard artifact quests./The ranger artifact quests./The samurai artifact quests./The ninja artifact quests./The dragoon artifact quests./The summoner artifact quests./The blue mage artifact quests./The corsair artifact quests./The puppetmaster artifact quests./The dancer artifact quests./The scholar artifact quests./The geomancer artifact quests./The rune fencer artifact quests.]"
 31: 0x0080 [0x25] WAIT_DIALOG_SELECT()
 32: 0x0081 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0093
 33: 0x0089 [0x03] Work_Zone[1] = 1073741824*
 34: 0x008E [0x21] END_EVENT
 35: 0x008F [0x00] END_REQSTACK()

SUBROUTINE_0093:
 36: 0x0093 [0x03] Work_Zone[1] = Work_Zone[0]
 37: 0x0098 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8578*]:
    → "All memories of your former trials will be lost."
 38: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x00A0 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8575*]:
    → "However, there are items that fate will not allow you to possess more than one of. If you wish to obtain these items again, you must first cast away those that you still hold on to."
 40: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x00A8 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8579*]:
    → "Are you certain this is what you wish?"
 42: 0x00AF [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x00B0 [0x24] CREATE_DIALOG(message_id=8580*, default_option=0*, option_flags=0*)
    → "Have your memories erased? [I need more time to think./I have made up my mind.]"
 44: 0x00B7 [0x25] WAIT_DIALOG_SELECT()
 45: 0x00B8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CA
 46: 0x00C0 [0x03] Work_Zone[1] = 1073741824*
 47: 0x00C5 [0x21] END_EVENT
 48: 0x00C6 [0x00] END_REQSTACK()

SUBROUTINE_00CA:
 49: 0x00CA [0x42] SET_CLI_EVENT_CANCEL_DATA()
 50: 0x00CB [0x73] EventEntity casts magic 253* on LocalPlayer
 51: 0x00D6 [0x2B] Vingijard (ID: 17780812/0x010F504C) [8581*]:
    → "Understood. Now close your eyes and relax..."
 52: 0x00DD [0x1C] WAIT(120* ticks)
 53: 0x00E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 54: 0x00F1 [0x1C] WAIT(180* ticks)
 55: 0x00F4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x00F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 57: 0x0106 [0x21] END_EVENT
 58: 0x0107 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0090 [0x01] GOTO 0x0093
# Dead code (unreachable instructions):
     0x00C7 [0x01] GOTO 0x00CA
```
