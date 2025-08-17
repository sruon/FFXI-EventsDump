# 16883810 - Havillione

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 156 bytes                   |
| Total Events     | 3                           |
| References Count | 7                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [320](#event-320)     | 0x0001       |     49 |             11 |
| [383](#event-383)     | 0x0032       |     49 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2B29      |       11049 |
|       1 | 0x0023      |          35 |
|       2 | 0x2B2A      |       11050 |
|       3 | 0x2B2B      |       11051 |
|       4 | 0x2B6D      |       11117 |
|       5 | 0x2B6E      |       11118 |
|       6 | 0x2B6F      |       11119 |

## String References

- **11049**: Young folk these days have become blind to the light of Altana.
- **11050**: They do not realize it is her blessing that fills this well with water for us to drink...
- **11051**: May Altana have mercy on their pitiful souls!
- **11117**: The elder Despachiaire's granddaughter has the most magnificent voice. It is as if you were hearing the whisper of the Dawn Goddess herself.
- **11118**: However, I remember there being another young girl in the Tavnazian choir who was just as talented as Lady Ulmia.
- **11119**: If only little Emeline had survived the beastman attack.

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

### Event 320

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 5B 01 80 F8 FF FF   ........#[.....
0010: 7F F8 FF FF 7F 74 68 6B  31 1D 02 80 23 5B 01 80  .....thk1...#[..
0020: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 1D 03 80 23  ........thk2...#
0030: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=11049*)
    → "Young folk these days have become blind to the light of Altana."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=35*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=11050*)
    → "They do not realize it is her blessing that fills this well with water for us to drink..."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=35*
  7: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=11051*)
    → "May Altana have mercy on their pitiful souls!"
  8: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0030 [0x21] END_EVENT
 10: 0x0031 [0x00] END_REQSTACK()
```

### Event 383

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       1E F0 FF FF 7F 1D  04 80 23 5B 01 80 F8 FF    ........#[....
0040: FF 7F F8 FF FF 7F 74 68  6B 31 1D 05 80 23 5B 01  ......thk1...#[.
0050: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 1D 06 80  .........thk2...
0060: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0032 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=11117*)
    → "The elder Despachiaire's granddaughter has the most magnificent voice. It is as if you were hearing the whisper of the Dawn Goddess herself."
  2: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x003B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=35*
  4: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=11118*)
    → "However, I remember there being another young girl in the Tavnazian choir who was just as talented as Lady Ulmia."
  5: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=35*
  7: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=11119*)
    → "If only little Emeline had survived the beastman attack."
  8: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0061 [0x21] END_EVENT
 10: 0x0062 [0x00] END_REQSTACK()
```
