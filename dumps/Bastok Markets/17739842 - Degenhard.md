# 17739842 - Degenhard

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Bastok Markets (ID: 235) |
| Block Size       | 248 bytes                |
| Total Events     | 8                        |
| References Count | 15                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [255](#event-255)     | 0x0001       |     11 |              5 |
| [256](#event-256)     | 0x000C       |     11 |              5 |
| [258](#event-258)     | 0x0017       |     35 |             10 |
| [342](#event-342)     | 0x003A       |      1 |              1 |
| [14](#event-14)       | 0x003B       |     39 |             15 |
| [20](#event-20)       | 0x0062       |     30 |             10 |
| [15](#event-15)       | 0x0080       |     12 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DF0      |        7664 |
|       1 | 0x1DEA      |        7658 |
|       2 | 0x1DEE      |        7662 |
|       3 | 0x1DEF      |        7663 |
|       4 | 0x00C9      |         201 |
|       5 | 0x0000      |           0 |
|       6 | 0x36EF      |       14063 |
|       7 | 0x36F0      |       14064 |
|       8 | 0x0DD5      |        3541 |
|       9 | 0x0DD6      |        3542 |
|      10 | 0x0DD7      |        3543 |
|      11 | 0x36F1      |       14065 |
|      12 | 0x36F2      |       14066 |
|      13 | 0x36F3      |       14067 |
|      14 | 0x36F4      |       14068 |

## String References

- **7658**: Hah! Yah! I'm still alive and kickin'! Do you want to know how I can be so energetic at my age? I'll tell you if you bring me the secret ingredient of my formula!
- **7662**: Yes, that is the secret ingredient! Ah, but it's not what you think--I don't eat this, as some seem to think.
- **7663**: I keep it in a pocket close to my heart to remind myself of my own mortality. That is my secret. Hmm... Maybe you're still a little too young to understand.
- **7664**: Hah! Yah! I'm still alive and kickin'!
- **14063**: Hah! Yah! Can't ye see I'm... Wait a minute. I almost didn't recognize ye...
- **14064**: Looks like someone's come a long way since our last meetin'. Why don't I give ye somethin' that might help in yer training?
- **14065**: But first, I'm gonna need proof that ye're ready. $0, $1, and $2 should do the trick.
- **14066**: Don't ye give me that face. It's trainin'--it ain't supposed to be easy!
- **14067**: Bring me $0, $1, and $2 and I'll give ye somethin' that should serve ye well.
- **14068**: Well, looks like someone's ready for [his/her] next challenge. As promised, here's somethin' for ya.

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

### Event 255

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7664*)
    → "Hah! Yah! I'm still alive and kickin'!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 256

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7658*)
    → "Hah! Yah! I'm still alive and kickin'! Do you want to know how I can be so energetic at my age? I'll tell you if you bring me the secret ingredient of my formula!"
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x21] END_EVENT
  4: 0x0016 [0x00] END_REQSTACK()
```

### Event 258

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 35 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      42  20 01 1E F0 FF FF 7F 1D         B .......
0020: 02 80 23 1D 03 80 23 45  04 80 F0 FF FF 7F F0 FF  ..#...#E........
0030: FF 7F 71 73 74 63 05 80  21 00                    ..qstc..!.      
```

#### Opcodes

```
  0: 0x0017 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0018 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7662*)
    → "Yes, that is the secret ingredient! Ah, but it's not what you think--I don't eat this, as some seem to think."
  4: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0023 [0x1D] PRINT_EVENT_MESSAGE(message_id=7663*)
    → "I keep it in a pocket close to my heart to remind myself of my own mortality. That is my secret. Hmm... Maybe you're still a little too young to understand."
  6: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0027 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x0038 [0x21] END_EVENT
  9: 0x0039 [0x00] END_REQSTACK()
```

### Event 342

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                00                           .     
```

#### Opcodes

```
  0: 0x003A [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 39 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   42 1E F0 FF FF             B....
0040: 7F 1D 06 80 23 1D 07 80  23 03 02 10 08 80 03 03  ....#...#.......
0050: 10 09 80 03 04 10 0A 80  1D 0B 80 23 1D 0C 80 23  ...........#...#
0060: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x003B [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x003C [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0041 [0x1D] PRINT_EVENT_MESSAGE(message_id=14063*)
    → "Hah! Yah! Can't ye see I'm... Wait a minute. I almost didn't recognize ye..."
  3: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=14064*)
    → "Looks like someone's come a long way since our last meetin'. Why don't I give ye somethin' that might help in yer training?"
  5: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0049 [0x03] Work_Zone[2] = 3541*
  7: 0x004E [0x03] Work_Zone[3] = 3542*
  8: 0x0053 [0x03] Work_Zone[4] = 3543*
  9: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=14065*)
    → "But first, I'm gonna need proof that ye're ready. $0, $1, and $2 should do the trick."
 10: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x005C [0x1D] PRINT_EVENT_MESSAGE(message_id=14066*)
    → "Don't ye give me that face. It's trainin'--it ain't supposed to be easy!"
 12: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0060 [0x21] END_EVENT
 14: 0x0061 [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 30 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       1E F0 FF FF 7F 03  02 10 08 80 03 03 10 09    ..............
0070: 80 03 04 10 0A 80 1D 0D  80 23 1D 0C 80 23 21 00  .........#...#!.
```

#### Opcodes

```
  0: 0x0062 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0067 [0x03] Work_Zone[2] = 3541*
  2: 0x006C [0x03] Work_Zone[3] = 3542*
  3: 0x0071 [0x03] Work_Zone[4] = 3543*
  4: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=14067*)
    → "Bring me $0, $1, and $2 and I'll give ye somethin' that should serve ye well."
  5: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=14066*)
    → "Don't ye give me that face. It's trainin'--it ain't supposed to be easy!"
  7: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x007E [0x21] END_EVENT
  9: 0x007F [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 42 1E F0 FF FF 7F 1D 0E  80 23 21 00              B........#!.    
```

#### Opcodes

```
  0: 0x0080 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0081 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0086 [0x1D] PRINT_EVENT_MESSAGE(message_id=14068*)
    → "Well, looks like someone's ready for [his/her] next challenge. As promised, here's somethin' for ya."
  3: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x008A [0x21] END_EVENT
  5: 0x008B [0x00] END_REQSTACK()
```
