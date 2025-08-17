# 17162741 - Tohs Jhannih

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 188 bytes                    |
| Total Events     | 4                            |
| References Count | 9                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [430](#event-430)     | 0x0001       |     42 |             10 |
| [161](#event-161)     | 0x002B       |     73 |             13 |
| [32](#event-32)       | 0x0074       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0020      |          32 |
|       2 | 0x2AAC      |       10924 |
|       3 | 0x2AAD      |       10925 |
|       4 | 0x003B      |          59 |
|       5 | 0x2B51      |       11089 |
|       6 | 0x1194      |        4500 |
|       7 | 0x2B52      |       11090 |
|       8 | 0x2B53      |       11091 |

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

### Event 430

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 42 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 6E F8 FF   J...........n..
0010: FF 7F 01 80 99 F8 FF FF  7F 2B F8 FF FF 7F 02 80  .........+......
0020: 23 2B F8 FF FF 7F 03 80  23 21 00                 #+......#!.     
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x6E] EventEntity uses emote 32*
  3: 0x0014 [0x99] Wait for EventEntity animation to complete
  4: 0x0019 [0x2B] EventEntity [10924*]:
    → "One...two...three.. Hm? Wait a minute, something's not rrright..."
  5: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0021 [0x2B] EventEntity [10925*]:
    → "Alright, I'm gonna count over. Gimme a minute here..."
  7: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0029 [0x21] END_EVENT
  9: 0x002A [0x00] END_REQSTACK()
```

### Event 161

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 73 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   4A F8 FF FF 7F             J....
0030: F0 FF FF 7F 1C 00 80 66  04 80 F8 FF FF 7F F8 FF  .......f........
0040: FF 7F 74 6C 6B 30 2B F8  FF FF 7F 05 80 23 03 02  ..tlk0+......#..
0050: 10 06 80 2B F8 FF FF 7F  07 80 23 2B F8 FF FF 7F  ...+......#+....
0060: 08 80 23 66 04 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0070: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x002B [0x4A] EventEntity looks at LocalPlayer
  1: 0x0034 [0x1C] WAIT(30* ticks)
  2: 0x0037 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x0046 [0x2B] EventEntity [11089*]:
    → "What? Food that our Gha Nabohan prrrince will enjoy?"
  4: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x004E [0x03] Work_Zone[2] = 4500*
  6: 0x0053 [0x2B] EventEntity [11090*]:
    → "Why, that would be $0, naturrrally!"
  7: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x005B [0x2B] EventEntity [11091*]:
    → "The irresistible, pungent aroma that permeates when you grrrill them makes my nostrils flare and-- <Slurp>...my mouth water!"
  9: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 11: 0x0072 [0x21] END_EVENT
 12: 0x0073 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0074  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:             00                                        .           
```

#### Opcodes

```
  0: 0x0074 [0x00] END_REQSTACK()
```
