# 16883806 - Calengeard

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 88 bytes                    |
| Total Events     | 3                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [260](#event-260)     | 0x0001       |     11 |              5 |
| [395](#event-395)     | 0x000C       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2B09      |       11017 |
|       1 | 0x2B7F      |       11135 |
|       2 | 0x001D      |          29 |
|       3 | 0x2B80      |       11136 |

## String References

- **11017**: This is the main entrance to the Tavnazian Safehold.
- **11135**: Sometimes at night, I still see visions of the battlefield I stood on twenty years ago. The cold eyes of the Kindred as they searched the landscape for their next victim...
- **11136**: I remember hearing tales of how the Shadow Lord called up these bloodthirsty beasts from the depths of hell, where their dark leader awaited in slumber...

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

### Event 260

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
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=11017*)
    → "This is the main entrance to the Tavnazian Safehold."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 395

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 66 02 80  F8 FF FF 7F F8 FF FF 7F  ....#f..........
0020: 74 77 62 30 1D 03 80 23  21 00                    twb0...#!.      
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=11135*)
    → "Sometimes at night, I still see visions of the battlefield I stood on twenty years ago. The cold eyes of the Kindred as they searched the landscape for their next victim..."
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb0" with entities [EventEntity, EventEntity], work=29*
  4: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=11136*)
    → "I remember hearing tales of how the Shadow Lord called up these bloodthirsty beasts from the depths of hell, where their dark leader awaited in slumber..."
  5: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0028 [0x21] END_EVENT
  7: 0x0029 [0x00] END_REQSTACK()
```
