# 17723499 - Beriphaule

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 472 bytes                     |
| Total Events     | 5                             |
| References Count | 27                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [606](#event-606)     | 0x0001       |    287 |             76 |
| [607](#event-607)     | 0x0120       |     13 |              6 |
| [608](#event-608)     | 0x012D       |     13 |              6 |
| [609](#event-609)     | 0x013A       |     13 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1B35      |        6965 |
|       1 | 0x1B36      |        6966 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x1B38      |        6968 |
|       5 | 0x1B39      |        6969 |
|       6 | 0x1B3A      |        6970 |
|       7 | 0x1B3B      |        6971 |
|       8 | 0x1B3C      |        6972 |
|       9 | 0x1B3D      |        6973 |
|      10 | 0x1B3F      |        6975 |
|      11 | 0x1B40      |        6976 |
|      12 | 0x19CE      |        6606 |
|      13 | 0x1B41      |        6977 |
|      14 | 0x1B42      |        6978 |
|      15 | 0x1B44      |        6980 |
|      16 | 0x1B45      |        6981 |
|      17 | 0x1B46      |        6982 |
|      18 | 0x00FD      |         253 |
|      19 | 0x00C8      |         200 |
|      20 | 0x0078      |         120 |
|      21 | 0x1B47      |        6983 |
|      22 | 0x1B43      |        6979 |
|      23 | 0x1B37      |        6967 |
|      24 | 0x1B49      |        6985 |
|      25 | 0x1B48      |        6984 |
|      26 | 0x1B4A      |        6986 |

## String References

- **6606**: You do not have enough gil.
- **6965**: Welcome to [San d'Oria/Bastok/Windurst]. Do you wish to change your allegiance from your current one to [San d'Oria/Bastok/Windurst]?
- **6966**: Ask about changing your allegiance? [Yes./No.]
- **6967**: Then, good journey, [sir/miss].
- **6968**: You can apply here to change your allegiance to [San d'Oria/Bastok/Windurst].
- **6969**: We will have to seal away some of your memories as an international security measure. Those memories will be unsealed should you change your allegiance back to your former country.
- **6970**: Incidentally, if this is your first time changing your allegiance, you will have to start over from rank 1 in your new nation.
- **6971**: Your rank in your former nation is still kept, so if you change your allegiance back you will return to your previous rank.
- **6972**: In addition, you will retain your current conquest points as well as any records of your expeditionary force quests. Oh, and you will be required to pay a processing fee of $5 gil along with your application for transfer.
- **6973**: You will also retain your current rank in [San d'Oria/Bastok/Windurst], which is presently rank $2.
- **6975**: Do you still wish to change your allegiance?
- **6976**: Change your allegiance to [San d'Oria/Bastok/Windurst]? [Yes./No.]
- **6977**: I am obligated to ask you again: Are you sure you want to go through with this?
- **6978**: Change your allegiance to [San d'Oria/Bastok/Windurst]? [Yes./No.]
- **6979**: I know it isn't an easy decision to make. Please think it through before you decide.
- **6980**: Very well. I will accept your application for [San d'Orian/Bastokan/Windurstian] citizenship.
- **6981**: I will now cast a spell to seal some of your memories away. Close your eyes...
- **6982**: May your decision be a wise one...
- **6983**: You are now a citizen of [San d'Oria/Bastok/Windurst]!
- **6984**: This is where citizens of other nations apply for citizenship in [San d'Oria/Bastok/Windurst]. Since you are [San d'Orian/Bastokan/Windurstian], there is not much I can do for you.
- **6985**: I cannot accept applications for [San d'Orian/Bastokan/Windurstian] citizenship while you are on a mission.
- **6986**: Your home country seems to be in trouble... I cannot accept [San d'Orian/Bastokan/Windurstian] citizenship applications at this time.

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

### Event 606

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 287 bytes |
| Instructions | 76        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 1D  00 80 23 24 01 80 02 80   B........#$....
0010: 03 80 25 02 00 10 03 80  00 08 01 03 01 10 03 80  ..%.............
0020: 1D 04 80 23 1D 05 80 23  02 03 10 03 80 00 3F 00  ...#...#......?.
0030: 1D 06 80 23 1D 07 80 23  1D 08 80 23 01 47 00 1D  ...#...#...#.G..
0040: 09 80 23 1D 08 80 23 1D  0A 80 23 24 0B 80 02 80  ..#...#...#$....
0050: 03 80 25 02 00 10 03 80  00 F1 00 02 06 10 03 80  ..%.............
0060: 00 6F 00 03 01 10 03 80  48 0C 80 20 00 21 00 03  .o......H.. .!..
0070: 01 10 03 80 1D 0D 80 23  24 0E 80 02 80 03 80 25  .......#$......%
0080: 02 00 10 03 80 00 DA 00  1D 0F 80 23 1D 10 80 23  ...........#...#
0090: 1D 11 80 23 73 12 80 F8  FF FF 7F F0 FF FF 7F 1C  ...#s...........
00A0: 13 80 45 13 80 F8 FF FF  7F F8 FF FF 7F 66 64 6F  ..E..........fdo
00B0: 32 03 80 1C 14 80 02 03  10 02 80 00 D2 00 45 13  2.............E.
00C0: 80 F8 FF FF 7F F8 FF FF  7F 66 64 69 32 03 80 48  .........fdi2..H
00D0: 15 80 03 01 10 02 80 01  EE 00 02 00 10 02 80 00  ................
00E0: EE 00 03 01 10 03 80 1D  16 80 23 01 EE 00 01 05  ..........#.....
00F0: 01 02 00 10 02 80 00 05  01 03 01 10 03 80 1D 16  ................
0100: 80 23 01 05 01 01 1C 01  02 00 10 02 80 00 1C 01  .#..............
0110: 03 01 10 03 80 1D 17 80  23 01 1C 01 20 00 21 00  ........#... .!.
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=6965*)
    → "Welcome to [San d'Oria/Bastok/Windurst]. Do you wish to change your allegiance from your current one to [San d'Oria/Bastok/Windurst]?"
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x24] CREATE_DIALOG(message_id=6966*, default_option=1*, option_flags=0*)
    → "Ask about changing your allegiance? [Yes./No.]"
  5: 0x0012 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0013 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0108
  7: 0x001B [0x03] Work_Zone[1] = 0*
  8: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=6968*)
    → "You can apply here to change your allegiance to [San d'Oria/Bastok/Windurst]."
  9: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=6969*)
    → "We will have to seal away some of your memories as an international security measure. Those memories will be unsealed should you change your allegiance back to your former country."
 11: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0028 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x003F
 13: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=6970*)
    → "Incidentally, if this is your first time changing your allegiance, you will have to start over from rank 1 in your new nation."
 14: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=6971*)
    → "Your rank in your former nation is still kept, so if you change your allegiance back you will return to your previous rank."
 16: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=6972*)
    → "In addition, you will retain your current conquest points as well as any records of your expeditionary force quests. Oh, and you will be required to pay a processing fee of $5 gil along with your application for transfer."
 18: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x003C [0x01] GOTO 0x0047
 20: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=6973*)
    → "You will also retain your current rank in [San d'Oria/Bastok/Windurst], which is presently rank $2."
 21: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=6972*)
    → "In addition, you will retain your current conquest points as well as any records of your expeditionary force quests. Oh, and you will be required to pay a processing fee of $5 gil along with your application for transfer."
 23: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0047:
 24: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=6975*)
    → "Do you still wish to change your allegiance?"
 25: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x004B [0x24] CREATE_DIALOG(message_id=6976*, default_option=1*, option_flags=0*)
    → "Change your allegiance to [San d'Oria/Bastok/Windurst]? [Yes./No.]"
 27: 0x0052 [0x25] WAIT_DIALOG_SELECT()
 28: 0x0053 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00F1
 29: 0x005B [0x02] IF !(Work_Zone[6] == 0*) GOTO 0x006F
 30: 0x0063 [0x03] Work_Zone[1] = 0*
 31: 0x0068 [0x48] [System] [6606*]:
    → "You do not have enough gil."
 32: 0x006B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x006D [0x21] END_EVENT
 34: 0x006E [0x00] END_REQSTACK()
 35: 0x006F [0x03] Work_Zone[1] = 0*
 36: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=6977*)
    → "I am obligated to ask you again: Are you sure you want to go through with this?"
 37: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x0078 [0x24] CREATE_DIALOG(message_id=6978*, default_option=1*, option_flags=0*)
    → "Change your allegiance to [San d'Oria/Bastok/Windurst]? [Yes./No.]"
 39: 0x007F [0x25] WAIT_DIALOG_SELECT()
 40: 0x0080 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00DA
 41: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=6980*)
    → "Very well. I will accept your application for [San d'Orian/Bastokan/Windurstian] citizenship."
 42: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=6981*)
    → "I will now cast a spell to seal some of your memories away. Close your eyes..."
 44: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x0090 [0x1D] PRINT_EVENT_MESSAGE(message_id=6982*)
    → "May your decision be a wise one..."
 46: 0x0093 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x0094 [0x73] EventEntity casts magic 253* on LocalPlayer
 48: 0x009F [0x1C] WAIT(200* ticks)
 49: 0x00A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 50: 0x00B3 [0x1C] WAIT(120* ticks)
 51: 0x00B6 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x00D2
 52: 0x00BE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 53: 0x00CF [0x48] [System] [6983*]:
    → "You are now a citizen of [San d'Oria/Bastok/Windurst]!"
 54: 0x00D2 [0x03] Work_Zone[1] = 1*
 55: 0x00D7 [0x01] GOTO 0x00EE
 56: 0x00DA [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00EE
 57: 0x00E2 [0x03] Work_Zone[1] = 0*
 58: 0x00E7 [0x1D] PRINT_EVENT_MESSAGE(message_id=6979*)
    → "I know it isn't an easy decision to make. Please think it through before you decide."
 59: 0x00EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x00EB [0x01] GOTO 0x00EE

SUBROUTINE_00EE:
 61: 0x00EE [0x01] GOTO 0x0105
 62: 0x00F1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0105
 63: 0x00F9 [0x03] Work_Zone[1] = 0*
 64: 0x00FE [0x1D] PRINT_EVENT_MESSAGE(message_id=6979*)
    → "I know it isn't an easy decision to make. Please think it through before you decide."
 65: 0x0101 [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x0102 [0x01] GOTO 0x0105

SUBROUTINE_0105:
 67: 0x0105 [0x01] GOTO 0x011C
 68: 0x0108 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x011C
 69: 0x0110 [0x03] Work_Zone[1] = 0*
 70: 0x0115 [0x1D] PRINT_EVENT_MESSAGE(message_id=6967*)
    → "Then, good journey, [sir/miss]."
 71: 0x0118 [0x23] WAIT_FOR_DIALOG_INTERACTION
 72: 0x0119 [0x01] GOTO 0x011C

SUBROUTINE_011C:
 73: 0x011C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 74: 0x011E [0x21] END_EVENT
 75: 0x011F [0x00] END_REQSTACK()
```

### Event 607

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 13 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 1E F0 FF FF 7F 1D 18 80  23 20 00 21 00           ........# .!.   
```

#### Opcodes

```
  0: 0x0120 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0125 [0x1D] PRINT_EVENT_MESSAGE(message_id=6985*)
    → "I cannot accept applications for [San d'Orian/Bastokan/Windurstian] citizenship while you are on a mission."
  2: 0x0128 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0129 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  4: 0x012B [0x21] END_EVENT
  5: 0x012C [0x00] END_REQSTACK()
```

### Event 608

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 13 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         1E F0 FF               ...
0130: FF 7F 1D 19 80 23 20 00  21 00                    .....# .!.      
```

#### Opcodes

```
  0: 0x012D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0132 [0x1D] PRINT_EVENT_MESSAGE(message_id=6984*)
    → "This is where citizens of other nations apply for citizenship in [San d'Oria/Bastok/Windurst]. Since you are [San d'Orian/Bastokan/Windurstian], there is not much I can do for you."
  2: 0x0135 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0136 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  4: 0x0138 [0x21] END_EVENT
  5: 0x0139 [0x00] END_REQSTACK()
```

### Event 609

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013A   |
| Data Size    | 13 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                1E F0 FF FF 7F 1D            ......
0140: 1A 80 23 20 00 21 00                              ..# .!.         
```

#### Opcodes

```
  0: 0x013A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x013F [0x1D] PRINT_EVENT_MESSAGE(message_id=6986*)
    → "Your home country seems to be in trouble... I cannot accept [San d'Orian/Bastokan/Windurstian] citizenship applications at this time."
  2: 0x0142 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0143 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  4: 0x0145 [0x21] END_EVENT
  5: 0x0146 [0x00] END_REQSTACK()
```
