# 17666739 - Milchupain

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Vunkerl (ID: 217) |
| Block Size       | 128 bytes                   |
| Total Events     | 3                           |
| References Count | 6                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1019](#event-1019)   | 0x0001       |     44 |             11 |
| [1022](#event-1022)   | 0x002D       |     29 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x001D      |          29 |
|       2 | 0x0000      |           0 |
|       3 | 0x1FC7      |        8135 |
|       4 | 0x1FC6      |        8134 |
|       5 | 0x1FCF      |        8143 |

## String References

- **8134**: Blast! Were it not for that accursed whisker, we'd make short work of these fiends! At least, so the commander says...
- **8135**: If you've a mind to venture inland, I suggest you take due caution. The stories that our scouts tell would have even the most battle-hardened knight quaking in his sollerets.
- **8143**: (Just between you and I, somehow Commander Rahal just doesn't inspire the confidence he once did. Fighting off the hordes has taken its toll on even the most stout-hearted of us, I fear...)

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

### Event 1019

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 44 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  02 02 10 02 80 00 27 00  ....tlk0......'.
0020: 1D 03 80 23 01 2B 00 1D  04 80 23 21 00           ...#.+....#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  3: 0x0018 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0027
  4: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=8135*)
    → "If you've a mind to venture inland, I suggest you take due caution. The stories that our scouts tell would have even the most battle-hardened knight quaking in his sollerets."
  5: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0024 [0x01] GOTO 0x002B
  7: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=8134*)
    → "Blast! Were it not for that accursed whisker, we'd make short work of these fiends! At least, so the commander says..."
  8: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_002B:
  9: 0x002B [0x21] END_EVENT
 10: 0x002C [0x00] END_REQSTACK()
```

### Event 1022

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         1E F0 FF               ...
0030: FF 7F 1C 00 80 66 01 80  F8 FF FF 7F F8 FF FF 7F  .....f..........
0040: 74 6C 6B 30 1D 05 80 23  21 00                    tlk0...#!.      
```

#### Opcodes

```
  0: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0032 [0x1C] WAIT(30* ticks)
  2: 0x0035 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  3: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=8143*)
    → "(Just between you and I, somehow Commander Rahal just doesn't inspire the confidence he once did. Fighting off the hordes has taken its toll on even the most stout-hearted of us, I fear...)"
  4: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0048 [0x21] END_EVENT
  6: 0x0049 [0x00] END_REQSTACK()
```
