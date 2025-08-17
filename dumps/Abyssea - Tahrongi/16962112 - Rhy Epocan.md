# 16962112 - Rhy Epocan

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 60 bytes                    |
| Total Events     | 2                           |
| References Count | 3                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [412](#event-412)     | 0x0001       |     21 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1FCF      |        8143 |
|       1 | 0x1FD0      |        8144 |
|       2 | 0x1FD1      |        8145 |

## String References

- **8143**: The shame! The terrrible, utterrr shame of it all!
- **8144**: I am a Sibyl Guard, rrraised from birth to protect the Star Sibyl with my life. Now here I stand, flung to the far rrreaches of heaven-knows-where with Her Holiness nowhere in sight!
- **8145**: Is this my punishment for failing in my duty!? No! I will not accept this miserrrable fate!

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

### Event 412

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 1D 01 80 23   .....op...#...#
0010: 1D 02 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=8143*)
    → "The shame! The terrrible, utterrr shame of it all!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=8144*)
    → "I am a Sibyl Guard, rrraised from birth to protect the Star Sibyl with my life. Now here I stand, flung to the far rrreaches of heaven-knows-where with Her Holiness nowhere in sight!"
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=8145*)
    → "Is this my punishment for failing in my duty!? No! I will not accept this miserrrable fate!"
  8: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0014 [0x21] END_EVENT
 10: 0x0015 [0x00] END_REQSTACK()
```
