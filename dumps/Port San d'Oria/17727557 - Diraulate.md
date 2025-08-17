# 17727557 - Diraulate

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 120 bytes                 |
| Total Events     | 2                         |
| References Count | 7                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [581](#event-581)     | 0x0001       |     64 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1EC2      |        7874 |
|       2 | 0x001E      |          30 |
|       3 | 0x1EC3      |        7875 |
|       4 | 0x1EC4      |        7876 |
|       5 | 0x1EC5      |        7877 |
|       6 | 0x1EC6      |        7878 |

## String References

- **7874**: The Goddess of the Dawn spoke: "He who fails to question his faith is blind. A believer without doubt will turn gold to lead."
- **7875**: "I can only light thy candle; thou must carry thy own."
- **7876**: "I cannot lead thee, for thy path is thine alone. Let the light of thy candle guide thee."
- **7877**: "He who finds me at the journey's end..." That is all. No one knows what follows.
- **7878**: But the day will come when all is revealed.

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

### Event 581

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 64 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1C 02 80 1D 03  ...tlk0...#.....
0020: 80 23 1C 02 80 1D 04 80  23 1C 02 80 1D 05 80 23  .#......#......#
0030: 1C 02 80 1D 06 80 23 5E  69 64 6C 30 1C 02 80 21  ......#^idl0...!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7874*)
    → "The Goddess of the Dawn spoke: "He who fails to question his faith is blind. A believer without doubt will turn gold to lead.""
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1C] WAIT(30* ticks)
  7: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7875*)
    → ""I can only light thy candle; thou must carry thy own.""
  8: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0022 [0x1C] WAIT(30* ticks)
 10: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7876*)
    → ""I cannot lead thee, for thy path is thine alone. Let the light of thy candle guide thee.""
 11: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0029 [0x1C] WAIT(30* ticks)
 13: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=7877*)
    → ""He who finds me at the journey's end..." That is all. No one knows what follows."
 14: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0030 [0x1C] WAIT(30* ticks)
 16: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=7878*)
    → "But the day will come when all is revealed."
 17: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0037 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 19: 0x003C [0x1C] WAIT(30* ticks)
 20: 0x003F [0x21] END_EVENT
 21: 0x0040 [0x00] END_REQSTACK()
```
