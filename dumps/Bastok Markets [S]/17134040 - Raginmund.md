# 17134040 - Raginmund

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 208 bytes                   |
| Total Events     | 6                           |
| References Count | 9                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [111](#event-111)     | 0x0001       |     33 |              9 |
| [112](#event-112)     | 0x0022       |      1 |              1 |
| [113](#event-113)     | 0x0023       |     33 |              9 |
| [114](#event-114)     | 0x0044       |     34 |             10 |
| [115](#event-115)     | 0x0066       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0000      |           0 |
|       2 | 0x3029      |       12329 |
|       3 | 0x302A      |       12330 |
|       4 | 0x2A81      |       10881 |
|       5 | 0x2A79      |       10873 |
|       6 | 0x2A82      |       10882 |
|       7 | 0x2A83      |       10883 |
|       8 | 0x2A84      |       10884 |

## String References

- **10873**: The caravan Karla was traveling with was set upon by a Quadav raiding party, and no one has seen her since. I don't have the heart to tell Aileen...
- **10881**: Aileen's friend, Karla, was called away to stay with family in the village of Lahnefeld, on the outskirts of Bastok.
- **10882**: Could this be the present Karla meant to give to Aileen!?
- **10883**: You've just missed her. I'm sure she would like to have it, though...
- **10884**: I haven't seen Aileen for a while now. I hope you can get that present to her somehow...
- **12329**: I hear lots of people saying they wish they hadn't been born to witness such dark and troubled days. But I, for one, am glad I'm alive to witness this war.
- **12330**: Undoubtedly there are hardships to be endured, but this is a heroic battle that will surely live on in our histories! I would count myself blessed to be able to see it through to completion!

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

### Event 111

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 D8 71 05 01   ........f...q..
0010: D8 71 05 01 74 6C 6B 30  1D 02 80 23 1D 03 80 23  .q..tlk0...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Raginmund (ID: 17134040/0x010571D8), Raginmund (ID: 17134040/0x010571D8)], work=0*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=12329*)
    → "I hear lots of people saying they wish they hadn't been born to witness such dark and troubled days. But I, for one, am glad I'm alive to witness this war."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=12330*)
    → "Undoubtedly there are hardships to be endured, but this is a heroic battle that will surely live on in our histories! I would count myself blessed to be able to see it through to completion!"
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       00                                            .             
```

#### Opcodes

```
  0: 0x0022 [0x00] END_REQSTACK()
```

### Event 113

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E F0 FF FF 7F  1C 00 80 66 01 80 D8 71     ........f...q
0030: 05 01 D8 71 05 01 74 6C  6B 30 1D 04 80 23 1D 05  ...q..tlk0...#..
0040: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0028 [0x1C] WAIT(30* ticks)
  2: 0x002B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Raginmund (ID: 17134040/0x010571D8), Raginmund (ID: 17134040/0x010571D8)], work=0*
  3: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=10881*)
    → "Aileen's friend, Karla, was called away to stay with family in the village of Lahnefeld, on the outskirts of Bastok."
  4: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=10873*)
    → "The caravan Karla was traveling with was set upon by a Quadav raiding party, and no one has seen her since. I don't have the heart to tell Aileen..."
  6: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0042 [0x21] END_EVENT
  8: 0x0043 [0x00] END_REQSTACK()
```

### Event 114

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 34 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             42 1E F0 FF  FF 7F 1C 00 80 66 01 80      B........f..
0050: D8 71 05 01 D8 71 05 01  74 6C 6B 30 1D 06 80 23  .q...q..tlk0...#
0060: 1D 07 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0044 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0045 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x004A [0x1C] WAIT(30* ticks)
  3: 0x004D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Raginmund (ID: 17134040/0x010571D8), Raginmund (ID: 17134040/0x010571D8)], work=0*
  4: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=10882*)
    → "Could this be the present Karla meant to give to Aileen!?"
  5: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=10883*)
    → "You've just missed her. I'm sure she would like to have it, though..."
  7: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0064 [0x21] END_EVENT
  9: 0x0065 [0x00] END_REQSTACK()
```

### Event 115

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   42 1E  F0 FF FF 7F 1C 00 80 66        B........f
0070: 01 80 D8 71 05 01 D8 71  05 01 74 6C 6B 30 1D 08  ...q...q..tlk0..
0080: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0066 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0067 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x006C [0x1C] WAIT(30* ticks)
  3: 0x006F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Raginmund (ID: 17134040/0x010571D8), Raginmund (ID: 17134040/0x010571D8)], work=0*
  4: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=10884*)
    → "I haven't seen Aileen for a while now. I hope you can get that present to her somehow..."
  5: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0082 [0x21] END_EVENT
  7: 0x0083 [0x00] END_REQSTACK()
```
