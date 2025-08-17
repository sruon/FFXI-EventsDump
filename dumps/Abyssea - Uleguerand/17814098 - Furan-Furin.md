# 17814098 - Furan-Furin

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 140 bytes                      |
| Total Events     | 5                              |
| References Count | 6                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [272](#event-272)     | 0x0001       |     28 |              8 |
| [273](#event-273)     | 0x001D       |     25 |              9 |
| [274](#event-274)     | 0x0036       |     25 |              9 |
| [270](#event-270)     | 0x004F       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0031      |          49 |
|       1 | 0x1EEB      |        7915 |
|       2 | 0x0020      |          32 |
|       3 | 0x1EEC      |        7916 |
|       4 | 0x0000      |           0 |
|       5 | 0x1EEE      |        7918 |

## String References

- **7915**: Can't you see that I'm busy monitoring this area for signs of impending avalanchey-wanches? You can't? Well, I just told you! So keep quietaru, please.
- **7916**: Ah, so you're the sucker--ah, the brave volunteer come to set up the bomb for us, are you? Take care not to overdo it with the firesand, will you? The lastaru guy nearly blasted-wasted me off the side of a cliff!
- **7918**: You were a huge help. Really, truly! Couldn't have done it bettaru myself, and that's saying something!

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

### Event 272

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 52 D2 0F 01 52   .....opf..R...R
0010: D2 0F 01 74 6C 6B 30 1D  01 80 23 21 00           ...tlk0...#!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Furan-Furin (ID: 17814098/0x010FD252), Furan-Furin (ID: 17814098/0x010FD252)], work=49*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7915*)
    → "Can't you see that I'm busy monitoring this area for signs of impending avalanchey-wanches? You can't? Well, I just told you! So keep quietaru, please."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x21] END_EVENT
  7: 0x001C [0x00] END_REQSTACK()
```

### Event 273

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         1E F0 FF               ...
0020: FF 7F 6F 70 6E 52 D2 0F  01 02 80 99 52 D2 0F 01  ..opnR......R...
0030: 1D 03 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x001D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0023 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0024 [0x6E] Furan-Furin (ID: 17814098/0x010FD252) uses emote 32*
  4: 0x002B [0x99] Wait for Furan-Furin (ID: 17814098/0x010FD252) animation to complete
  5: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=7916*)
    → "Ah, so you're the sucker--ah, the brave volunteer come to set up the bomb for us, are you? Take care not to overdo it with the firesand, will you? The lastaru guy nearly blasted-wasted me off the side of a cliff!"
  6: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0034 [0x21] END_EVENT
  8: 0x0035 [0x00] END_REQSTACK()
```

### Event 274

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   1E F0  FF FF 7F 6F 70 6E 52 D2        .....opnR.
0040: 0F 01 04 80 99 52 D2 0F  01 1D 05 80 23 21 00     .....R......#!. 
```

#### Opcodes

```
  0: 0x0036 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003D [0x6E] Furan-Furin (ID: 17814098/0x010FD252) uses emote 0*
  4: 0x0044 [0x99] Wait for Furan-Furin (ID: 17814098/0x010FD252) animation to complete
  5: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "You were a huge help. Really, truly! Couldn't have done it bettaru myself, and that's saying something!"
  6: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004D [0x21] END_EVENT
  8: 0x004E [0x00] END_REQSTACK()
```

### Event 270

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               00                 .
```

#### Opcodes

```
  0: 0x004F [0x00] END_REQSTACK()
```
