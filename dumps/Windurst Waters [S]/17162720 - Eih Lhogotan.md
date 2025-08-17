# 17162720 - Eih Lhogotan

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 248 bytes                    |
| Total Events     | 4                            |
| References Count | 8                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [407](#event-407)     | 0x0001       |     60 |             10 |
| [227](#event-227)     | 0x003D       |     60 |             10 |
| [228](#event-228)     | 0x0079       |     60 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x003B      |          59 |
|       2 | 0x2AC4      |       10948 |
|       3 | 0x2AC5      |       10949 |
|       4 | 0x2AF8      |       11000 |
|       5 | 0x2AF9      |       11001 |
|       6 | 0x2AFA      |       11002 |
|       7 | 0x2AFB      |       11003 |

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

### Event 407

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 66 01 80   J...........f..
0010: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 2B F8 FF FF  ........tlk0+...
0020: 7F 02 80 23 2B F8 FF FF  7F 03 80 23 66 01 80 F8  ...#+......#f...
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x001C [0x2B] EventEntity [10948*]:
    → "Just take a look around you... The city sustained significant damage during the Theomilitary's assault the other day."
  4: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0024 [0x2B] EventEntity [10949*]:
    → "Only this district has been somewhat repaired since then. Windurst Walls still remains in ruins, almost totally submerged beneath the waters."
  6: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  8: 0x003B [0x21] END_EVENT
  9: 0x003C [0x00] END_REQSTACK()
```

### Event 227

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         4A F8 FF               J..
0040: FF 7F F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F  .........f......
0050: F8 FF FF 7F 74 6C 6B 30  2B F8 FF FF 7F 04 80 23  ....tlk0+......#
0060: 2B F8 FF FF 7F 05 80 23  66 01 80 F8 FF FF 7F F8  +......#f.......
0070: FF FF 7F 74 6C 6B 31 21  00                       ...tlk1!.       
```

#### Opcodes

```
  0: 0x003D [0x4A] EventEntity looks at LocalPlayer
  1: 0x0046 [0x1C] WAIT(30* ticks)
  2: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x0058 [0x2B] EventEntity [11000*]:
    → "A state of emerrrgency's been declared, or haven't you heard? This is no time to be trrraipsing about the city!"
  4: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0060 [0x2B] EventEntity [11001*]:
    → "Civilians have been ordered to take shelter in Heavens Tower. You'd best be off to wherever you belong--confusion in the strrreets will only serve to heighten the danger."
  6: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0068 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  8: 0x0077 [0x21] END_EVENT
  9: 0x0078 [0x00] END_REQSTACK()
```

### Event 228

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             4A F8 FF FF 7F F0 FF           J......
0080: FF 7F 1C 00 80 66 01 80  F8 FF FF 7F F8 FF FF 7F  .....f..........
0090: 74 6C 6B 30 2B F8 FF FF  7F 06 80 23 2B F8 FF FF  tlk0+......#+...
00A0: 7F 07 80 23 66 01 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
00B0: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x0079 [0x4A] EventEntity looks at LocalPlayer
  1: 0x0082 [0x1C] WAIT(30* ticks)
  2: 0x0085 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x0094 [0x2B] EventEntity [11002*]:
    → "Grrr... Those birdmen did a number on Windurst Walls, I'll tell you. Shattered roofs, collapsed brrridges... The place is in shambles!"
  4: 0x009B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x009C [0x2B] EventEntity [11003*]:
    → "But the citizens are already hard at work repairing the damages. We'll see the Walls restored to their former glorrry before you know it!"
  6: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00A4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  8: 0x00B3 [0x21] END_EVENT
  9: 0x00B4 [0x00] END_REQSTACK()
```
