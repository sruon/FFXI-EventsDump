# 17162723 - Rakh Mhappyoh

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 124 bytes                    |
| Total Events     | 4                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [411](#event-411)     | 0x0001       |     68 |             12 |
| [231](#event-231)     | 0x0045       |      1 |              1 |
| [232](#event-232)     | 0x0046       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x003B      |          59 |
|       2 | 0x2ACC      |       10956 |
|       3 | 0x2ACD      |       10957 |
|       4 | 0x2ACE      |       10958 |

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

### Event 411

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 68 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 66 01 80   J...........f..
0010: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 2B F8 FF FF  ........tlk0+...
0020: 7F 02 80 23 2B F8 FF FF  7F 03 80 23 2B F8 FF FF  ...#+......#+...
0030: 7F 04 80 23 66 01 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
0040: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x001C [0x2B] EventEntity [10956*]:
    → "Have you ever met Romaa Mihgo? She heads the Cobras, the strongest and most ruthless division of the Mithra Mercenaries."
  4: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0024 [0x2B] EventEntity [10957*]:
    → "Her behavior may be a bit...not to some's liking. But her prowess is virtually without match. Windurst owes her a great debt of gratitude for her service."
  6: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002C [0x2B] EventEntity [10958*]:
    → "Oddly enough, though, it seems Romaa Mihgo isn't exactly a fan of the Federation. I wonder what it was that convinced her to pledge herself to our cause..."
  8: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0034 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
 10: 0x0043 [0x21] END_EVENT
 11: 0x0044 [0x00] END_REQSTACK()
```

### Event 231

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 232

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   00                                    .         
```

#### Opcodes

```
  0: 0x0046 [0x00] END_REQSTACK()
```
