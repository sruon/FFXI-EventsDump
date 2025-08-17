# 17162737 - Narito-Pettito

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 172 bytes                    |
| Total Events     | 3                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [425](#event-425)     | 0x0001       |     60 |             10 |
| [229](#event-229)     | 0x003D       |     60 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0028      |          40 |
|       2 | 0x2A9B      |       10907 |
|       3 | 0x2A9C      |       10908 |
|       4 | 0x2AFC      |       11004 |

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

### Event 425

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
  2: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x001C [0x2B] EventEntity [10907*]:
    → "Welcome to the Optistery. We are one of the world's largest repositories of knowledge and wisdom, housing an unmatched collection of tomes, scrolls, scriptures, chronicles, records, atlases, and just about any other type of printed material you could think of! But..."
  4: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0024 [0x2B] EventEntity [10908*]:
    → "We are temporarily closed due to Minister Karaha-Baruha's absence. Our deepest apologies for any inconvenience."
  6: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  8: 0x003B [0x21] END_EVENT
  9: 0x003C [0x00] END_REQSTACK()
```

### Event 229

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
0050: F8 FF FF 7F 74 6C 6B 30  2B F8 FF FF 7F 02 80 23  ....tlk0+......#
0060: 2B F8 FF FF 7F 04 80 23  66 01 80 F8 FF FF 7F F8  +......#f.......
0070: FF FF 7F 74 6C 6B 31 21  00                       ...tlk1!.       
```

#### Opcodes

```
  0: 0x003D [0x4A] EventEntity looks at LocalPlayer
  1: 0x0046 [0x1C] WAIT(30* ticks)
  2: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x0058 [0x2B] EventEntity [10907*]:
    → "Welcome to the Optistery. We are one of the world's largest repositories of knowledge and wisdom, housing an unmatched collection of tomes, scrolls, scriptures, chronicles, records, atlases, and just about any other type of printed material you could think of! But..."
  4: 0x005F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0060 [0x2B] EventEntity [11004*]:
    → "We are closed to the public in mourning of our late Minister Karaha-Baruha. Even during his long absence, the thought of his return was enough to motivate us to take the utmost pride in our duties tending the archives. Whatever will become of us now?"
  6: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0068 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  8: 0x0077 [0x21] END_EVENT
  9: 0x0078 [0x00] END_REQSTACK()
```
